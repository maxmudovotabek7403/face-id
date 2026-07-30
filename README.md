# 🧠 Face-ID Recognition System

A real-time Face Recognition system built with **Python**, **InsightFace**, and **OpenCV**. The project detects faces from a webcam or video stream, identifies registered users, and can be integrated into attendance systems, access control, or AI surveillance applications.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![InsightFace](https://img.shields.io/badge/InsightFace-Face%20Recognition-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📸 Demo

> **Live Demo Video**

https://github.com/yourusername/face-id/assets/demo.mp4

or

<p align="center">
  <img src="assets/demo.gif" width="800">
</p>

---

# ✨ Features

- 🎯 Real-time face detection
- 👤 Face recognition using InsightFace
- 📷 Webcam support
- 📁 Register new faces
- ⚡ Fast cosine similarity matching
- 🚫 Unknown face detection
- 📊 Easy integration with attendance systems
- 💻 Lightweight and easy to deploy

---

# 🏗️ Project Structure

```
face-id/
│
├── database/
│   ├── person1/
│   ├── person2/
│   └── ...
│
├── embeddings.pkl
├── register.py
├── recognize.py
├── utils.py
├── requirements.txt
├── README.md
└── assets/
    └── demo.gif
```

---

# 🛠️ Tech Stack

- Python
- OpenCV
- InsightFace
- NumPy
- ONNX Runtime

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/face-id.git
```

Go to the project

```bash
cd face-id
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Register faces

```bash
python register.py
```

Start recognition

```bash
python recognize.py
```

---

# 🧠 How It Works

1. Detect faces using InsightFace
2. Extract facial embeddings
3. Compare embeddings with registered users
4. Compute cosine similarity
5. Display user's name if similarity exceeds the threshold
6. Otherwise label as **Unknown**

---

# 📈 Performance

| Feature | Status |
|---------|--------|
| Face Detection | ✅ |
| Face Recognition | ✅ |
| Real-time | ✅ |
| Unknown Detection | ✅ |
| Webcam Support | ✅ |

---

# 📸 Screenshots

| Recognition |
|-------------|
| ![](assets/screenshot1.png) |

---

# 🔮 Future Improvements

- Multi-camera support
- Face tracking
- Attendance logging
- Web dashboard
- REST API
- GPU acceleration
- Docker support

---

# 🤝 Contributing

Contributions are welcome!

Fork the repository and submit a Pull Request.

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
