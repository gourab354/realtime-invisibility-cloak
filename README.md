# 🌌 Ghost // Invisibility Cloak System

A high-performance, real-time computer vision application that grants you the power of digital invisibility. Built with **Python**, **OpenCV**, and **MediaPipe**, this system uses advanced AI segmentation and hand gesture tracking to let you vanish from your webcam stream at the pinch of a finger.

![Project Demo](demo.gif)

---

## ✨ Features

- **🤖 AI-Powered Silhouette Isolation**: Uses MediaPipe Selfie Segmentation with an enhanced morphology pipeline (dilation and Gaussian blur closing) to guarantee 100% full-coverage masking, eliminating edge bleeding or loose clothing artifacts.
- **🖐️ Gesture-Driven Activation**: 
  - Spread both hands apart to summon a dynamic, sci-fi glowing **Portal Box** between your index fingertips.
  - Pinch your thumb and index finger together on either hand to toggle **Invisibility Mode** instantly.
- **👁️ Cinematic CyberHUD**: A fully immersive tactical heads-up display complete with corner framing brackets, fingertip targeting reticles, real-time FPS monitoring, compute device indicators, and an interactive opacity progress bar.
- **🔊 Asynchronous Sci-Fi Sound Effects**: Immersive, multi-threaded audio cues (calibration countdowns, activation sweeps, and camera shutters) powered by `winsound` that run in background threads to completely avoid frame drop or video lag.
- **📹 Production Utilities**: Built-in features to save high-resolution screenshots or track session states instantly with dedicated hotkeys.

---

## 🛠️ Tech Stack

- **Core Language:** Python 3.8+
- **Computer Vision:** OpenCV (cv2)
- **Machine Learning Models:** MediaPipe (Selfie Segmentation & Hands Tracking)
- **Numerical Operations:** NumPy

---

## 🚀 Installation & Setup

1. **Clone or download** this repository to your local machine.
2. **Connect a webcam** to your computer.
3. **Run the application** (Dependencies will auto-install on the first launch if missing!):

```bash
python main.py
To specify a custom camera index (e.g., if using an external webcam), pass the index as an argument:Bashpython main.py 1
🎮 How to Control & Play1. Gesture ReferenceStepActionVisual FeedbackStep 1Stand completely still for 3 seconds during startup.Countdown timer registers your room's background calibration.Step 2Raise both hands and spread them apart.A sleek, reactive yellow/cyan Portal Box aligns between your index fingers.Step 3Pinch your thumb and index finger together.You smoothly vanish into the environment!Step 4Pinch your fingers together once more.The system blends you smoothly back into the frame.2. Keyboard HotkeysR : Recalibrate Background (Clears cache and recaptures the empty room background).S : Save Screenshot (Captures the current output frame as a high-res .png).Q / ESC : Quit the application safely.🗂️ Project Architecturemain.py: The application entry point managing the webcam feed loop, key inputs, and core orchestration.engine.py: The engineering core hosting the SegmentationEngine (with custom mask boosting), HandTracker (pinch-ratio mechanics), BackgroundModel (temporal averaging), and PortalBox renderer.hud.py / CyberHUD: Renders the advanced sci-fi interface, corner markers, recording state overlays, and custom targeting reticles.cloaks.py & background.py: Modular engines handling background allocation policies and pure pixel-blending algorithms.sound.py: Multi-threaded sound card manager ensuring zero-latency audio playback for UI events.
