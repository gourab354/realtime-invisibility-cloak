# 🌌 Ghost // Invisibility Cloak System

<p align="center">
  <img src="Demo.gif" alt="Project Demo Loop" width="700px" style="border-radius: 10px; box-shadow: 0px 4px 20px rgba(0,0,0,0.3);"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white&style=for-the-badge" alt="Python Version">
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white&style=for-the-badge" alt="OpenCV Version">
  <img src="https://img.shields.io/badge/MediaPipe-AI%20Vision-purple?style=for-the-badge" alt="MediaPipe">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License">
</p>

---

## ⚡ Overview

**Ghost** is a high-performance, real-time computer vision application that grants you the power of digital invisibility. Built using **Python**, **OpenCV**, and **MediaPipe**, this system leverages advanced AI-driven silhouette isolation and hand gesture tracking to let you seamlessly vanish from your webcam stream at the pinch of a finger[cite: 6, 7].

---

## ✨ Key Features

* **🤖 AI-Powered Silhouette Isolation**: Utilizes MediaPipe Selfie Segmentation augmented by an advanced mathematical morphology pipeline (dilation and Gaussian blur closing). This guarantees 100% full-coverage masking, eliminating edge bleeding, color fringing, or loose clothing artifacts[cite: 3].
* **🖐️ Gesture-Driven Activation Loop**: 
    * **Summon**: Spread both hands apart to generate a dynamic, sci-fi glowing **Portal Box** right between your index fingertips[cite: 3, 7].
    * **Vanish**: Pinch your thumb and index finger together on either hand to toggle **Invisibility Mode** instantly[cite: 3, 7].
* **👁️ Cinematic CyberHUD**: An immersive tactical heads-up display overlay featuring corner framing brackets, fingertip tracking target reticles, real-time FPS telemetry metrics, compute device indicators, and an interactive opacity progress bar[cite: 4].
* **🔊 Asynchronous Sci-Fi Audio**: Immersive audio cues (calibration countdown ticks, activation sweeps, and camera shutters) powered by `winsound`. Audio execution runs entirely on multi-threaded background loops to prevent video frame drops or streaming latency[cite: 8].

---

## 🎮 How to Control & Play

### 1. Gesture Sequence Workflow

| Step | Gesture Action | UI Visual Feedback |
| :--- | :--- | :--- |
| **01** | **Stand completely still** for 3 seconds during initial boot[cite: 6, 7]. | A countdown sound registers your environment's clean baseline[cite: 6, 8]. |
| **02** | Raise both hands up and **spread them apart**[cite: 6, 7]. | A reactive cyan/yellow **Portal Box** aligns between your index fingers[cite: 3]. |
| **03** | **Pinch** your thumb and index finger together[cite: 3, 6, 7]. | The system blends you smoothly out, leaving only the clean room[cite: 2, 3]. |
| **04** | **Pinch your fingers together** once more[cite: 3, 6, 7]. | The alpha mask steps down, blending you back into reality[cite: 2, 3]. |

### 2. Operational Hotkeys

* `R` — **Recalibrate Background**: Flushes the baseline cache and re-samples an empty room frame[cite: 4, 6, 7].
* `S` — **Save Screenshot**: Captures the final frame buffer as a high-resolution `.png` file[cite: 4, 6, 7].
* `Q` / `ESC` — **Safe Quit**: Halts frame capture threads and destroys active window variables gracefully[cite: 4, 6, 7].

---

## 🚀 Installation & Launch

1. Clone or download this project workspace to your local directory.
2. Plug in your webcam setup[cite: 6, 7].
3. Fire up your terminal loop (required modules will auto-verify and **auto-install** on initialization):

```bash
python main.py
💡 External Camera Prompt: If using an external rig or secondary capture card, map the camera index integer directly into the console arguments[cite: 6, 7]:Bashpython main.py 1
🗂️ Workspace ArchitectureCode snippetgraph TD
    A[main.py: App Orchestration] --> B[engine.py: Compute & CV Core]
    B --> C[hud.py: CyberHUD Overlay]
    B --> D[sound.py: Async Audio Processing]
    B --> E[cloaks.py & background.py: Matrix Blenders]
main.py — Primary application orchestration layer. Handles camera capturing pipes and hardware polling hooks[cite: 6].engine.py — The analytical core houses tracking architectures, pinch thresholds, and custom matrix morphology routines[cite: 3].hud.py — Renders target bounding brackets, geometric HUD graphics, and live telemetry indicators.  sound.py — Background sound card wrapper managing zero-latency playback[cite: 8].cloaks.py & background.py — Pixel blending configurations and space-saving image buffering models.  📝 License & AttributionThis architecture is open-source software distributed under the terms of the MIT License[cite: 5].Designed and engineered with 💙 by Gourab.
