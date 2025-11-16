# **VisionTrack – Face Recognition Attendance System**

VisionTrack is an AI-powered **Face Recognition Attendance System** built using **Python, OpenCV, and face_recognition**.  
It detects and recognizes faces in real time using a webcam and automatically marks attendance in a CSV file.  
A clean **Tkinter GUI dashboard** displays the live camera feed and attendance records.

---

## 🚀 Features

### 🔍 Real-Time Face Recognition
Recognizes known individuals from live webcam video using deep-learning-based facial encodings.

### 📝 Automatic Attendance Logging
Once a face is recognized, the system logs:
- **Name**
- **Date**
- **Time**

Attendance is stored in `attendance.csv`, ensuring **no duplicate entries** per person per day.

### 🖥️ Tkinter Dashboard (GUI)
A simple and clean interface that shows:
- Live camera preview  
- Attendance table  
- Auto-refreshing logs  

### ⚡ Performance Optimized
- Processes every 3rd frame for better speed  
- Smooth bounding boxes using cached data  
- Adjustable tolerance for recognition accuracy  

### 📁 Easy Dataset Handling
Just place your images inside the `dataset/` folder.

---

## 🛠️ Tech Stack

- **Python 3**
- **OpenCV**
- **face_recognition**
- **NumPy**
- **Tkinter**
- **Pillow (PIL)**
- **CSV**

---

## 📂 Project Structure

VisionTrack/
│
├── dataset/
│ ├── Devang/
│ │ └── devang.jpg
│ ├── Pushpa/
│ │ └── pushpa.jpg
│ ├── Salman/
│ │ └── salman.jpg
│ └── Shahrukh/
│ └── shahrukh.jpg
│
├── attendance.csv
├── main.py
└── README.md

yaml
Copy code

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install opencv-python
pip install face_recognition
pip install numpy
pip install pillow
2️⃣ Add Known Faces
Place images inside the dataset folder:

bash
Copy code
dataset/Devang/devang.jpg
dataset/Pushpa/pushpa.jpg
dataset/Salman/salman.jpg
dataset/Shahrukh/shahrukh.jpg
3️⃣ Run the Application
bash
Copy code
python main.py
🧠 How It Works
Loads known face images and generates encodings

Opens the webcam and reads live frames

Detects faces and computes embeddings

Compares embeddings with known faces

Marks attendance once per day

Displays everything on the Tkinter dashboard

📈 Future Enhancements
Add face registration directly from webcam

Store attendance in a database (MySQL/PostgreSQL)

Add admin login panel

Export attendance as PDF

Add voice feedback (“Attendance marked for Devang”)

Add dark mode UI

Convert project into a Windows EXE
