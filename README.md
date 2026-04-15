# Hamster Gesture Cam

Real-time gesture detection that triggers hamster reaction images using your webcam.  
Built with [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/).

---

## Gestures

<table>
  <tr>
    <th align="left">Gesture</th>
    <th align="left">Image</th>
  </tr>
  <tr><td>Two Fingers</td><td><code>two.jpg</code></td></tr>
  <tr><td>Thumbs Up</td><td><code>ok.jpg</code></td></tr>
  <tr><td>Thumbs Down</td><td><code>bad.jpg</code></td></tr>
  <tr><td>Index Finger</td><td><code>index.jpg</code></td></tr>
  <tr><td>Tongue Out</td><td><code>tongue.jpg</code></td></tr>
</table>

---

## Getting Started

### Prerequisites
Python 3.8+ and a webcam.

```bash
pip install opencv-python mediapipe==0.10.10 numpy
```

### Installation

```bash
git clone https://github.com/rruexox/hamster-gesture-cam.git
cd hamster-gesture-cam
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
