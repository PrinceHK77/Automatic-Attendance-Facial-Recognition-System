Automatic Attendance using Facial Recognition

A Smart, Seamless & Secure Attendance System powered by AI and Computer Vision

![image](https://github.com/user-attachments/assets/18a4aa17-d300-400d-8a2b-1fad1748075d)

🚀 Overview
Welcome to the future of attendance management!

This project reimagines traditional attendance systems by integrating Facial Recognition powered by Artificial Intelligence and Computer Vision using Python. Designed for schools, colleges, and corporate offices, the system captures real-time video, detects and recognizes faces, and automatically logs attendance — all within seconds.

No more ID cards, manual entries, or proxy attendances. Just stand in front of the camera, and you're marked present.

🔧 Tech Stack
🐍 Python

🤖 OpenCV

🧠 Face Recognition (dlib)

🌐 Flask (for web interface)

🗃️ SQLite / CSV (for logging attendance)

💡 Features
🎥 Real-time face detection & recognition

📋 Automatic attendance marking with timestamp

🗂️ Attendance logs exportable to Excel/CSV

🌐 Lightweight Flask-based web UI

🔒 Secure & accurate recognition using facial embeddings

🧑‍🏫 Ideal for classrooms, labs, meetings & events

📸 How It Works
Face Registration:
Register each individual's face by capturing images through the camera.

Encoding Faces:
Extract facial embeddings and store them in a serialized format for quick access.

Live Camera Feed:
Launch real-time video stream to detect and compare faces.

Mark Attendance:
If a face matches a registered profile, attendance is automatically marked with a timestamp.

![image](https://github.com/user-attachments/assets/3f33d218-1ea9-4979-94db-d37a7628244e)

📂 Project Structure
📁 Facial-Recognition-Attendance
├── app.py                  # Flask server
├── encode_faces.py         # Face encoding script
├── recognize_faces.py      # Real-time recognition script
├── dataset/                # Stored face images
├── encodings.pickle        # Serialized facial encodings
├── attendance.csv          # Attendance log file
├── templates/              # Flask HTML templates
└── static/                 # CSS / JS / Media assets
🖥️ Installation

📊 Sample Output

![image](https://github.com/user-attachments/assets/3e1f8ad3-de5d-45d8-a9f9-1dadb03c1bf9)

Real-time recognition

Live timestamp logging

Smooth, lag-free performance

🌍 Use Cases
🎓 Schools & Colleges

🏢 Offices & Meetings

🧪 Labs & Research Centers

🎤 Events & Conferences
