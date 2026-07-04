import cv2
import numpy as np

class CloakEngine:
    def __init__(self, h, w):
        self.h, self.w = h, w
        self.mode = 0
        self.mode_names = ["PURE INVISIBILITY CLOAK"]

    def cycle_mode(self):
        return self.mode_names[0]

    def render_cloak(self, frame, seg_mask, bg, alpha):
        """Render pure invisibility by replacing the person's silhouette with the calibrated background."""
        if alpha <= 0.01 or bg is None:
            return frame

        roi_f = frame.astype(np.float32)
        roi_bg = bg.astype(np.float32) if bg.shape == frame.shape else cv2.resize(bg, (self.w, self.h)).astype(np.float32)
        
        # When cloaking is fading in/out, use 1.5x mask boost. When fully invisible, ensure 100% coverage
        eff_mask = np.clip(seg_mask * 1.5, 0, 1)
        roi_mask = eff_mask[:, :, np.newaxis]

        # Blend the frame with the stored background where the person was
        blend = roi_f * (1 - roi_mask * alpha) + roi_bg * (roi_mask * alpha)
        np.clip(blend, 0, 255, out=blend)
        frame[:, :] = blend.astype(np.uint8)

        return frame
