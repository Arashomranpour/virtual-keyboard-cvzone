<div align="center">

# ⌨️ Virtual Keyboard with Hand Tracking

**Type in the air - an on-screen keyboard you operate with your fingertips through the webcam.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![cvzone](https://img.shields.io/badge/cvzone-HandTracking-informational)

</div>

---

## ✨ How it works

- 🖐️ The webcam feed is analyzed with cvzone's `HandDetector`.
- ☝️ Hover your **index fingertip** over a key to highlight it.
- 🤏 **Pinch** your index finger and thumb together (distance < 33 px) to press the key - the character is sent to the active window via `pynput`.
- ⌫ The `-` key acts as **backspace**.
- 🔤 Three rows of keys are drawn over the video; press **Q** in the preview window to quit.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/virtual-keyboard-cvzone.git
cd virtual-keyboard-cvzone
pip install opencv-python cvzone mediapipe pynput
python keyboard.py
```

Click into a text field (Notepad, browser...) so the typed characters have somewhere to go.

## 📁 Project Structure

```
.
└── keyboard.py     # Hand detection, on-screen keys, pinch-to-type
```

## 🛠️ Tech Stack

`OpenCV` · `cvzone` · `MediaPipe` · `pynput`
