import subprocess, sys, importlib.util, os

REQUIRED = {"cv2":"opencv-python","numpy":"numpy","mediapipe":"mediapipe"}

def _auto_install():
    missing = [pkg for mod,pkg in REQUIRED.items()
               if importlib.util.find_spec(mod) is None]
    if missing:
        print(f"\n[AUTO-INSTALL] Installing: {', '.join(missing)}\n")
        subprocess.check_call([sys.executable,"-m","pip","install","--quiet"]+missing)
        print("[AUTO-INSTALL] Done.\n")

_auto_install()

import cv2, numpy as np, time
from engine import BackgroundModel, SegmentationEngine, HandTracker, PortalBox, HUD

BANNER = """
====================================================================
      Ghost / Invisibility Mode  dev: tubakhxn
====================================================================
  GESTURES:
    1. Stand still 3s             ->  background captured
    2. Show BOTH hands spread     ->  yellow portal box appears
    3. PINCH thumb + index tip    ->  YOU VANISH INTO THE BACKGROUND!
    4. Pinch again                ->  reappear

  KEYS:
    [R] Recalibrate background
    [S] Save high-res screenshot
    [Q] / [ESC] Quit
====================================================================
"""
WINDOW = "Ghost / Invisibility Mode  by Tuba"

def run_calibration(cap, bg_model, w, h, seconds=3):
    print(f"[CAL] Stand still {seconds}s for room background calibration...")
    start = time.time()
    while time.time() - start < seconds:
        ret, frame = cap.read()
        if not ret: continue
        bg_model.update(frame.astype(np.float32))
        rem = int(seconds - (time.time() - start)) + 1
        disp = (frame * 0.4).astype(np.uint8)
        msg  = "STAND STILL  —  CALIBRATING BACKGROUND"
        tw   = cv2.getTextSize(msg, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0][0]
        cv2.putText(disp, msg, ((w-tw)//2, h//2-50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,230,255), 2, cv2.LINE_AA)
        tw2 = cv2.getTextSize(str(rem), cv2.FONT_HERSHEY_SIMPLEX, 4.0, 5)[0][0]
        cv2.putText(disp, str(rem), ((w-tw2)//2, h//2+80),
                    cv2.FONT_HERSHEY_SIMPLEX, 4.0, (0,255,120), 5, cv2.LINE_AA)
        cv2.imshow(WINDOW, disp)
        if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
            return False
    print("[CAL] Calibration complete!\n")
    return True

def _detect_device():
    try:
        import torch
        if torch.cuda.is_available():
            return "GPU/" + torch.cuda.get_device_name(0).split()[0]
    except ImportError:
        pass
    return "CPU"

def main():
    print(BANNER)
    dev_str = _detect_device()
    print(f"[INFO] Compute Device: {dev_str}")

    cam_idx  = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    cap      = None
    backends = ([(cv2.CAP_DSHOW, "DirectShow"), (cv2.CAP_MSMF, "MSMF"), (cv2.CAP_ANY, "Auto")]
                if sys.platform == "win32" else [(cv2.CAP_ANY, "Auto")])
    probe = None
    for backend, name in backends:
        print(f"[CAM] Attempting connection via {name}...")
        _c = cv2.VideoCapture(cam_idx + backend)
        if _c.isOpened():
            _c.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
            _c.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            _c.set(cv2.CAP_PROP_FPS, 30)
            ret, probe = _c.read()
            if ret and probe is not None:
                cap = _c
                print(f"[CAM] Webcam initialized successfully with {name}!")
                break
            _c.release()

    if cap is None:
        print("[ERROR] Could not open webcam. Ensure your camera is connected and not in use by other apps.")
        sys.exit(1)

    h, w = probe.shape[:2]
    print(f"[INFO] Camera Resolution: {w}x{h}")
    print("[INIT] Loading AI Segmentation and Hand Tracking models...")

    seg      = SegmentationEngine()
    tracker  = HandTracker()
    bg_model = BackgroundModel(h, w, n_frames=90)
    portal   = PortalBox()
    hud      = HUD(h, w, dev_str)

    print("[INIT] Models loaded! Launching application...\n")
    cv2.namedWindow(WINDOW, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW, min(w, 1280), min(h, 720))

    if not run_calibration(cap, bg_model, w, h, seconds=3):
        cap.release(); cv2.destroyAllWindows(); return

    if bg_model.buf:
        bg_model.bg    = np.mean(bg_model.buf, axis=0).astype(np.float32)
        bg_model.ready = True

    sc_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.02); continue

        hud.tick()

        seg_mask = seg.get_mask(frame)
        results  = tracker.process(frame)
        info     = tracker.get_info(results, w, h)

        portal.update(info)
        portal.update_alpha()

        out = portal.render(frame, seg_mask, bg_model.get(), info["all_points"])
        out = hud.draw(out, portal, info)

        cv2.imshow(WINDOW, out)
        key = cv2.waitKey(1) & 0xFF

        if key in (ord('q'), 27):
            break
        elif key in (ord('s'), ord('S')):
            fn = f"screenshot_{sc_idx:04d}.png"
            cv2.imwrite(fn, out)
            print(f"[SCREENSHOT] Saved {fn}")
            sc_idx += 1
        elif key in (ord('r'), ord('R')):
            bg_model.__init__(h, w)
            portal.invisible = False
            portal._alpha    = 0.0
            if not run_calibration(cap, bg_model, w, h, 3):
                break
            if bg_model.buf:
                bg_model.bg    = np.mean(bg_model.buf, axis=0).astype(np.float32)
                bg_model.ready = True

    cap.release()
    cv2.destroyAllWindows()
    print("\n[DONE] Goodbye!")

if __name__ == "__main__":
    main()