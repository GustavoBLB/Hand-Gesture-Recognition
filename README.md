# GestuRecognizer — LIBRAS Hand Gesture Recognition

A compact end-to-end prototype that **captures hand landmarks**, **trains a classifier**, and **recognizes the LIBRAS alphabet in real time** through a simple desktop UI.

> **Status:** in development — currently recognizes **letters**; next milestones include **full gestures/signs** beyond the alphabet.

---

## ✨ Features
- **Capture** hand landmarks from the webcam (OpenCV + MediaPipe), saving a **CSV dataset** (x, y, z for 21 landmarks).
- **Train** a **KNN** model (scikit-learn) with accuracy, classification report, and confusion matrix.
- **Recognize** letters in real time, overlaying the prediction on the video feed.
- **Desktop UI (Tkinter)** with three actions: **Capture**, **Train**, **Recognize**.

---

## 🎬 Demo & Screens
- **Demo video:** add your link here (e.g., LinkedIn post or `docs/demo.mp4`)
- **Screenshot:** place an image at `docs/screenshot.png` and it will render below.

![App Screenshot](docs/screenshot.png)

---

## 🗂️ Project Structure
    .
    ├─ main.py                   # Tkinter window that orchestrates: Capture → Train → Recognize
    ├─ gesture_capture.py        # Opens webcam, captures 21 landmarks (x,y,z), appends rows to database.csv
    ├─ train_model.py            # Loads CSV, trains scikit-learn KNN, shows metrics, saves model.pkl
    ├─ gesture_recognition.py    # Live inference: draws landmarks and overlays the predicted letter
    ├─ database.csv              # (auto-created) Labeled samples dataset
    ├─ model.pkl                 # (auto-created) Trained KNN model
    └─ requirements.txt          # Pinned dependencies for Python 3.10 

### What each file does
- **main.py** — small controller (Tkinter) with 3 buttons that run the scripts below.
- **gesture_capture.py** — keys: `s` save sample, `m` enter multi-saving (set label once, then press `s` repeatedly), `l` leave multi-saving, `q` quit.
- **train_model.py** — train/test split, trains **KNN (k=3)**, prints **accuracy**, **classification report**, **confusion matrix**; saves **model.pkl**.
- **gesture_recognition.py** — live prediction; if **max probability < 0.9**, shows **unknown** to avoid overconfident guesses.

---

## 🧰 Tech Stack
- **Python 3.10* 
- **OpenCV**
- **MediaPipe Hands**
- **NumPy / Pandas**
- **scikit-learn (KNN)**
- **Joblib**
- **Tkinter**

---

## ⚙️ Installation (Python 3.10 + virtual env)

MediaPipe doesn’t always support the newest Python releases. Use **Python 3.10** in a virtual environment for a smooth setup.

### 1) Install Python 3.10
-  download 3.10.x from python.org (check “Add Python to PATH” during install).

### 2) Create & activate a virtual environment

**Windows (PowerShell)**
    py -3.10 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip

**macOS / Linux**
    python3.10 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip

### 3) Install dependencies

With the requirements.txt file already included in the project, you can install all dependencies by running:
    pip install -r requirements.txt

### 4) Run the app
    python main.py

**Tips**
- If camera index 0 fails, change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` (or 2, …).
- In capture: `s` saves, `m` enables multi-saving (set label once), `l` exits multi-saving, `q` quits.

---

## 🧭 Roadmap
- [ ] Add **full gesture/sign** recognition (beyond letters)
- [ ] Improve dataset tooling (balancing, augmentation)
- [ ] Export/import datasets and models via the UI

---

## 🤝 Acknowledgements
- [MediaPipe Hands](https://developers.google.com/mediapipe)
- [scikit-learn](https://scikit-learn.org/)
