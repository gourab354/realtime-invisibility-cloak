# 🌌 Ghost // Invisibility Cloak System

<p align="center">
  <img src="Demo.gif" alt="Project Demo Loop" width="700px"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white&style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white&style=for-the-badge" alt="OpenCV">
  <img src="https://img.shields.io/badge/MediaPipe-AI%20Vision-purple?style=for-the-badge" alt="MediaPipe">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT">
</p>

---

# ⚡ Overview

**Ghost** is a high-performance, real-time computer vision application that grants you the power of digital invisibility. Built using **Python**, **OpenCV**, and **MediaPipe**, this system leverages AI-driven silhouette isolation and hand gesture tracking to let you seamlessly disappear from your webcam stream with nothing more than a pinch gesture.

---

# ✨ Key Features

- 🤖 **AI-Powered Silhouette Isolation**
  - MediaPipe Selfie Segmentation
  - Morphological refinement
  - Gaussian blur edge smoothing
  - Clean full-body masking

- 🖐️ **Gesture-Based Controls**
  - ✨ Spread both hands to create a glowing Portal Box.
  - 👌 Pinch thumb + index finger to toggle invisibility.

- 👁️ **CyberHUD Interface**
  - FPS Counter
  - Target Reticles
  - Hand Tracking Indicators
  - Opacity Progress Bar
  - Live Status Monitor

- 🔊 **Asynchronous Audio Engine**
  - Countdown
  - Camera shutter
  - Activation sounds
  - Non-blocking background playback

---

# 🎮 Controls

## Gesture Workflow

| Step | Gesture | Action |
|------|---------|--------|
| 1 | Stay still for 3 seconds | Background Calibration |
| 2 | Spread both hands | Portal appears |
| 3 | Pinch fingers | Become invisible |
| 4 | Pinch again | Become visible |

---

## Keyboard Shortcuts

| Key | Function |
|-----|----------|
| **R** | Recalibrate Background |
| **S** | Save Screenshot |
| **Q** | Quit |
| **ESC** | Quit |

---

# 🚀 Installation & Launch

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Ghost.git
cd Ghost
```

### 2️⃣ Run

```bash
python main.py
```

### External Camera

If you're using an external webcam:

```bash
python main.py 1
```

---

# 📂 Project Structure

```text
Ghost/
│
├── main.py              # Main Application
├── engine.py            # Vision Engine
├── hud.py               # HUD Renderer
├── sound.py             # Audio Engine
├── cloaks.py            # Cloak Effects
├── background.py        # Background Capture
│
├── Demo.gif
├── LICENSE
└── README.md
```

---

# 🧩 Module Overview

| Module | Description |
|---------|-------------|
| **main.py** | Initializes camera, application loop and orchestrates every subsystem. |
| **engine.py** | Handles MediaPipe segmentation, hand tracking, pinch detection and invisibility logic. |
| **hud.py** | Draws CyberHUD overlays, FPS counter, targeting brackets and telemetry. |
| **sound.py** | Plays activation, countdown and camera sounds asynchronously. |
| **cloaks.py** | Pixel blending engine responsible for invisibility rendering. |
| **background.py** | Captures and manages calibrated background frames. |

---

# 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Winsound
- Threading

---

# 📜 License

Licensed under the **MIT License**.

Feel free to modify, distribute and build upon this project.

---

# 👨‍💻 Author

<p align="center">

### 💙 Designed & Engineered by Gourab

Electronics • Robotics • Computer Vision • AI

</p>

---

<p align="center">
⭐ If you enjoyed this project, consider giving it a star!
</p>
