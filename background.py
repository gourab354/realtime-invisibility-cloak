import cv2
import numpy as np

class BackgroundManager:
    def __init__(self, h, w):
        self.h, self.w = h, w
        self.mode = 0
        self.mode_names = ["CALIBRATED WEBCAM ROOM"]

    def cycle_mode(self):
        return self.mode_names[0]

    def get_background(self, webcam_bg):
        """Always return the clean background captured from the room during calibration."""
        return webcam_bg
