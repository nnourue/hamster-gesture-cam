# Hamster Gesture Cam

Real-time gesture detection that triggers hamster reaction images using your webcam.  
Built with [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/).

---

## Gestures

| Gesture | Image |
|---|---|
| Two Fingers | `two.jpg` |
| Thumbs Up | `ok.jpg` |
| Thumbs Down | `bad.jpg` |
| Index Finger | `index.jpg` |
| Tongue Out | `tongue.jpg` |

---

## Getting Started

### Prerequisites
Python 3.8+ and a webcam.

```bash
pip install opencv-python mediapipe==0.10.10 numpy
```

### Installation

```bash
git clone https://github.com/your-username/hamster-gesture-cam.git
cd hamster-gesture-cam
```

### Image Setup

Add your reaction images to a `pics/` folder:

```
pics/
├── two.jpg
├── ok.jpg
├── bad.jpg
├── index.jpg
└── tongue.jpg
```

### Run

```bash
python cam.py
```

Press `q` to quit.

---

## Upcoming

- Fix glitches
- More hamster reaction images
- More gestures
