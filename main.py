import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

# ------------------------------------------
# Load Known Faces
# ------------------------------------------

known_encodings = []
known_names = []

def add_face(path, name):
    img = face_recognition.load_image_file(path)
    enc = face_recognition.face_encodings(img)
    if len(enc) > 0:
        known_encodings.append(enc[0])
        known_names.append(name)
        print(f"Added: {name}")
    else:
        print(f"No face detected in: {path}")

# Add your dataset
add_face(r"C:\Users\Devang\Desktop\face recognition project\dataset\Devang\devang.jpg", "Devang")
add_face(r"C:\Users\Devang\Desktop\face recognition project\dataset\pushpa\pushpa.jpg", "Pushpa")
add_face(r"C:\Users\Devang\Desktop\face recognition project\dataset\salman\salman.jpg", "Salman")
add_face(r"C:\Users\Devang\Desktop\face recognition project\dataset\shahrukh\shahrukh.jpg", "Shahrukh")

# ------------------------------------------
# Attendance System
# ------------------------------------------

ATTENDANCE_FILE = "attendance.csv"

if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time"])

def mark_attendance(name):
    today = datetime.now().strftime("%Y-%m-%d")

    with open(ATTENDANCE_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if name in line and today in line:
                return

    now = datetime.now()
    time = now.strftime("%H:%M:%S")

    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, today, time])

    print(f"Attendance marked: {name} at {time}")

# ------------------------------------------
# Tkinter GUI + Dashboard
# ------------------------------------------

window = tk.Tk()
window.title("Face Attendance System")
window.geometry("1200x700")
window.configure(bg="white")

title = tk.Label(window, text="Face Recognition Attendance System",
                 font=("Arial", 20, "bold"), bg="white")
title.pack(pady=10)

frame_main = tk.Frame(window, bg="white")
frame_main.pack(fill=tk.BOTH, expand=True)

frame_left = tk.Frame(frame_main, bg="white")
frame_left.pack(side=tk.LEFT, padx=20)

camera_label = tk.Label(frame_left)
camera_label.pack()

frame_right = tk.Frame(frame_main, bg="white")
frame_right.pack(side=tk.RIGHT, padx=20)

dash_title = tk.Label(frame_right, text="Live Attendance Dashboard",
                      font=("Arial", 16, "bold"), bg="white")
dash_title.pack(pady=10)

columns = ("Name", "Date", "Time")
tree = ttk.Treeview(frame_right, columns=columns, show="headings", height=25)

for col in columns:
    tree.heading(col, text=col)
tree.column("Name", width=150)
tree.column("Date", width=120)
tree.column("Time", width=120)

tree.pack()

def load_attendance():
    for row in tree.get_children():
        tree.delete(row)

    with open(ATTENDANCE_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            tree.insert("", tk.END, values=row)

def auto_refresh():
    load_attendance()
    window.after(1500, auto_refresh)

# ------------------------------------------
# Camera + FAST Face Recognition
# ------------------------------------------

cap = cv2.VideoCapture(0)

process_every_n_frames = 3
frame_count = 0

last_boxes = []
last_names = []

def run_camera():
    global frame_count, last_boxes, last_names

    tolerance = 0.55  # accuracy improvement

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame_count += 1

        # ------------------------------------------
        # Process every 3rd frame (Fast Recognition)
        # ------------------------------------------
        if frame_count % process_every_n_frames == 0:
            small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

            locations = face_recognition.face_locations(rgb_small)
            encodings = face_recognition.face_encodings(rgb_small, locations)

            temp_boxes = []
            temp_names = []

            for (top, right, bottom, left), face_enc in zip(locations, encodings):
                distances = face_recognition.face_distance(known_encodings, face_enc)
                best_match = np.argmin(distances)

                name = "Unknown"
                if distances[best_match] < tolerance:
                    name = known_names[best_match]
                    mark_attendance(name)

                # Scale box back
                top *= 4; right *= 4; bottom *= 4; left *= 4

                temp_boxes.append((top, right, bottom, left))
                temp_names.append(name)

            last_boxes = temp_boxes
            last_names = temp_names

        # ------------------------------------------
        # Draw Boxes & Names Every Frame (Smooth)
        # ------------------------------------------
        for (top, right, bottom, left), name in zip(last_boxes, last_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Convert to Tkinter preview
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(img))
        camera_label.config(image=img)
        camera_label.image = img

# Start camera thread
camera_thread = threading.Thread(target=run_camera, daemon=True)
camera_thread.start()

# Start auto dashboard refresh
auto_refresh()

window.mainloop()

cap.release()
cv2.destroyAllWindows()
