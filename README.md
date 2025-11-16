# **VisionTrack – Face Recognition Attendance System**

VisionTrack is an AI-powered **Face Recognition Attendance System** built with **Python, OpenCV, and face_recognition**.  
It detects and recognizes faces in real time using a webcam and automatically marks attendance in a CSV file.  
A modern **Tkinter GUI dashboard** displays live camera feed and attendance records.

---

## 🚀 Features

### 🔍 Real-Time Face Recognition
Recognizes known individuals from live webcam video using deep-learning-based face encodings.

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
- Processes every 3rd frame for faster recognition  
- Smooth rendering using cached face boxes  
- Customizable tolerance value  

### 📁 Easy Dataset Handling
Add known faces by simply placing images inside the `dataset/` directory.

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
│ ├── Person1/
│ │ └── image.jpg
│ ├── Person2/
│ │ └── image.jpg
│ └── ...
│
├── attendance.csv
├── main.py
└── README.md


---

## ▶️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install opencv-python
pip install face_recognition
pip install numpy
pip install pillow
