import cv2
import numpy as np
import time
import collections

class CyberHUD:
    FONT = cv2.FONT_HERSHEY_SIMPLEX
    MONO = cv2.FONT_HERSHEY_DUPLEX
    
    # Theme colors (BGR)
    CYAN = (0, 230, 255)
    GREEN = (0, 255, 120)
    RED = (0, 50, 255)
    WHITE = (240, 240, 240)
    DARK = (30, 30, 30)

    def __init__(self, h, w, dev_str):
        self.h, self.w = h, w
        self.dev_str = dev_str
        self._fps_buf = collections.deque(maxlen=30)
        self._last_t = time.time()
        self.rec_start_time = 0
        self.is_recording = False

    def tick(self):
        now = time.time()
        self._fps_buf.append(1.0 / max(now - self._last_t, 1e-6))
        self._last_t = now

    @property
    def fps(self):
        return np.mean(self._fps_buf) if self._fps_buf else 0.0

    def set_recording(self, status):
        if status and not self.is_recording:
            self.rec_start_time = time.time()
        self.is_recording = status

    def draw_corner_brackets(self, frame, color=(0, 230, 255), length=30, thick=2):
        """Draw sci-fi framing brackets in the 4 corners of the screen."""
        h, w = self.h, self.w
        m = 10  # margin
        cv2.line(frame, (m, m), (m+length, m), color, thick, cv2.LINE_AA)
        cv2.line(frame, (m, m), (m, m+length), color, thick, cv2.LINE_AA)
        cv2.line(frame, (w-m, m), (w-m-length, m), color, thick, cv2.LINE_AA)
        cv2.line(frame, (w-m, m), (w-m, m+length), color, thick, cv2.LINE_AA)
        cv2.line(frame, (m, h-m), (m+length, h-m), color, thick, cv2.LINE_AA)
        cv2.line(frame, (m, h-m), (m, h-m-length), color, thick, cv2.LINE_AA)
        cv2.line(frame, (w-m, h-m), (w-m-length, h-m), color, thick, cv2.LINE_AA)
        cv2.line(frame, (w-m, h-m), (w-m, h-m-length), color, thick, cv2.LINE_AA)

    def draw_reticle(self, frame, center, color, size=15):
        """Draw a high-tech targeting reticle around a point (like a fingertip)."""
        x, y = center
        cv2.circle(frame, (x, y), size, color, 1, cv2.LINE_AA)
        cv2.circle(frame, (x, y), 3, color, -1, cv2.LINE_AA)
        cv2.line(frame, (x-size-5, y), (x-size+3, y), color, 1, cv2.LINE_AA)
        cv2.line(frame, (x+size-3, y), (x+size+5, y), color, 1, cv2.LINE_AA)
        cv2.line(frame, (x, y-size-5), (x, y-size+3), color, 1, cv2.LINE_AA)
        cv2.line(frame, (x, y+size-3), (x, y+size+5), color, 1, cv2.LINE_AA)

    def draw(self, frame, portal, info: dict, cloak_engine, bg_manager):
        h, w = self.h, self.w
        alpha = portal._alpha
        hand_count = info["hand_count"]
        touching = info["fingers_touching"]
        tips = info["tips"]

        # Draw sci-fi framing brackets
        self.draw_corner_brackets(frame, color=self.CYAN)

        # Draw reticles on index tips
        if tips is not None:
            for p in tips:
                self.draw_reticle(frame, p, self.CYAN, size=18)

        # Top header bar background
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, 50), self.DARK, -1)
        cv2.addWeighted(overlay, 0.65, frame, 0.35, 0, frame)
        cv2.line(frame, (0, 50), (w, 50), self.CYAN, 1, cv2.LINE_AA)

        # Title & Device
        cv2.putText(frame, "GHOST // INVISIBILITY CLOAK SYSTEM", (24, 32), self.FONT, 0.65, self.CYAN, 2, cv2.LINE_AA)
        cv2.putText(frame, f"[ {self.dev_str} ]", (w - 380, 32), self.FONT, 0.45, self.WHITE, 1, cv2.LINE_AA)
        cv2.putText(frame, f"FPS {self.fps:05.1f}", (w - 140, 32), self.FONT, 0.55, self.GREEN, 1, cv2.LINE_AA)

        # Recording Indicator
        if self.is_recording:
            dur = int(time.time() - self.rec_start_time)
            mins, secs = dur // 60, dur % 60
            rec_str = f"REC [{mins:02d}:{secs:02d}]"
            if int(time.time() * 2) % 2 == 0:
                cv2.circle(frame, (w - 170, 75), 8, self.RED, -1, cv2.LINE_AA)
            cv2.putText(frame, rec_str, (w - 150, 80), self.FONT, 0.55, self.RED, 2, cv2.LINE_AA)

        # Cloak Status Indicator
        if alpha > 0.05:
            pulse = int(abs(np.sin(time.time() * 6)) * 100 + 155)
            cv2.circle(frame, (w - 20, 75), 7, (0, pulse, 255), -1)
            cv2.putText(frame, "INVISIBILITY CLOAK ACTIVE", (w - 210, 80), self.FONT, 0.45, (0, 230, 255), 1, cv2.LINE_AA)
        elif portal.active:
            cv2.circle(frame, (w - 20, 75), 7, self.GREEN, -1)
            cv2.putText(frame, "PORTAL READY — PINCH TO VANISH", (w - 260, 80), self.FONT, 0.42, self.GREEN, 1, cv2.LINE_AA)

        # Bottom footer bar background
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, h - 55), (w, h), self.DARK, -1)
        cv2.addWeighted(overlay, 0.70, frame, 0.30, 0, frame)
        cv2.line(frame, (0, h - 55), (w, h - 55), self.CYAN, 1, cv2.LINE_AA)

        # Cloak Opacity Bar
        bx, by, bw2 = 24, h - 35, 160
        cv2.rectangle(frame, (bx, by), (bx + bw2, by + 12), (50, 50, 50), -1)
        filled = int(bw2 * alpha)
        if filled > 0:
            cv2.rectangle(frame, (bx, by), (bx + filled, by + 12), self.CYAN, -1)
        cv2.putText(frame, f"CLOAK {int(alpha * 100):3d}%", (bx, by - 5), self.FONT, 0.42, self.CYAN, 1, cv2.LINE_AA)

        # Hand Count & Time
        cv2.putText(frame, f"HANDS: {hand_count}", (bx + 180, by + 10), self.FONT, 0.45, self.WHITE, 1, cv2.LINE_AA)
        cv2.putText(frame, time.strftime("%H:%M:%S"), (w - 90, by + 10), self.MONO, 0.45, (150, 150, 150), 1, cv2.LINE_AA)

        # Interactive controls help text
        controls_str = "[V] Rec Video | [S] Screenshot | [R] Recalibrate | [Q] Quit"
        tw = cv2.getTextSize(controls_str, self.FONT, 0.42, 1)[0][0]
        cv2.putText(frame, controls_str, ((w - tw) // 2, h - 18), self.FONT, 0.42, (200, 200, 200), 1, cv2.LINE_AA)

        # Pinch detection toast alert
        if touching:
            msg = ">>> PINCH DETECTED! TOGGLING INVISIBILITY <<<"
            tw2 = cv2.getTextSize(msg, self.FONT, 0.60, 2)[0][0]
            cv2.putText(frame, msg, ((w - tw2) // 2, h - 65), self.FONT, 0.60, self.GREEN, 2, cv2.LINE_AA)

        return frame
