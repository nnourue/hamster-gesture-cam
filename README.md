# 🐹 Hamster Gesture Cam

Real-time gesture detection that triggers hamster reaction images using your webcam.  
Built with [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/).
  
---

## Gestures

Show the camera one of these and see what happens:

- **Two Fingers** — `two.jpg`
- **Thumbs Up** — `ok.jpg`
- **Thumbs Down** — `bad.jpg`
- **Index Finger** — `index.jpg`
- **Tongue Out** — `tongue.jpg`

---

## Getting Started

### Prerequisites

- Python 3.8+
- A working webcam

### Installation

```bash
git clone https://github.com/nnourue/hamster-gesture-cam.git
cd hamster-gesture-cam
pip install opencv-python mediapipe==0.10.10 numpy
```

### Usage

```bash
python cam.py
```

Press `q` to quit (or close the window if you can't handle the hamsters).

---

## Roadmap

- [ ] Stability improvements and glitch fixes
- [ ] More hamster reaction images
- [ ] Support for more gestures
