import threading
import time
import sys

try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False

def _async_run(func, *args):
    """Run a sound function asynchronously in a daemon thread to prevent video lag."""
    t = threading.Thread(target=func, args=args, daemon=True)
    t.start()

def play_beep(freq=1000, duration=100):
    """Play a single beep sound."""
    if not HAS_WINSOUND:
        return
    def _beep():
        try:
            winsound.Beep(int(freq), int(duration))
        except Exception:
            pass
    _async_run(_beep)

def play_calibration_tick():
    """Play a high-tech tick during calibration countdown."""
    if not HAS_WINSOUND:
        return
    def _tick():
        try:
            winsound.Beep(1200, 50)
        except Exception:
            pass
    _async_run(_tick)

def play_calibration_done():
    """Play an ascending chime when calibration completes."""
    if not HAS_WINSOUND:
        return
    def _done():
        try:
            winsound.Beep(600, 80)
            time.sleep(0.02)
            winsound.Beep(850, 80)
            time.sleep(0.02)
            winsound.Beep(1200, 150)
        except Exception:
            pass
    _async_run(_done)

def play_portal_ready():
    """Play a subtle buzz when the hand portal box becomes active."""
    if not HAS_WINSOUND:
        return
    def _ready():
        try:
            winsound.Beep(900, 60)
        except Exception:
            pass
    _async_run(_ready)

def play_cloak_on():
    """Play an ascending sci-fi sweep when vanishing."""
    if not HAS_WINSOUND:
        return
    def _sweep_up():
        try:
            for freq in range(400, 1500, 180):
                winsound.Beep(freq, 22)
        except Exception:
            pass
    _async_run(_sweep_up)

def play_cloak_off():
    """Play a descending sci-fi sweep when reappearing."""
    if not HAS_WINSOUND:
        return
    def _sweep_down():
        try:
            for freq in range(1400, 350, -180):
                winsound.Beep(freq, 22)
        except Exception:
            pass
    _async_run(_sweep_down)

def play_mode_switch():
    """Play a double beep when switching cloaking modes."""
    if not HAS_WINSOUND:
        return
    def _switch():
        try:
            winsound.Beep(800, 40)
            time.sleep(0.01)
            winsound.Beep(1100, 60)
        except Exception:
            pass
    _async_run(_switch)

def play_shutter():
    """Play a camera shutter / record toggle sound."""
    if not HAS_WINSOUND:
        return
    def _shutter():
        try:
            winsound.Beep(1800, 30)
            time.sleep(0.02)
            winsound.Beep(1400, 40)
        except Exception:
            pass
    _async_run(_shutter)
