# hamster-gesture-cam

Real-time gesture detection that triggers hamster reaction images using your webcam.

[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)


## Gestures
| Gesture | Emoji | Image |
|---------|-------|-------|
| Two fingers | ✌️ | two.jpg |
| Thumbs up | 👍 | ok.jpg |
| Thumbs down | 👎 | bad.jpg |
| Index finger | ☝️ | index.jpg |
| Tongue out | 👅 | tongue.jpg |

## Requirements
```bash
pip install opencv-python mediapipe numpy
```

## Usage
Put your reaction images in a `pics/` folder:
```
pics/
├── two.jpg
├── ok.jpg
├── bad.jpg
├── index.jpg
└── tongue.jpg
```
Then run:
```bash
python cam.py
```
Press `q` to quit.