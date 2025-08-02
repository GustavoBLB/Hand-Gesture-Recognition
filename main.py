import tkinter as tk
import subprocess
import sys
import os

# Caminho absoluto para o Python do ambiente virtual
python_path = sys.executable

def exec_capture_gesture():
    subprocess.Popen([python_path, "gesture_capture.py"])

def exec_train_model():
    subprocess.Popen([python_path, "train_model.py"])

def exec_gesture_recognition():
    subprocess.Popen([python_path, "gesture_recognition.py"])

# Criar janela
window = tk.Tk()
window.title("Gesture Recognition Controller")
width_window = 400
height_window = 200

width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

pos_x = (width_screen // 2) - (width_window // 2)
pos_y = (height_screen // 2) - (height_window // 2)

window.geometry(f"{width_window}x{height_window}+{pos_x}+{pos_y}")

# Botões
tk.Button(window, text="Capture Gesture", command=exec_capture_gesture).pack(pady=10)
tk.Button(window, text="Train Model", command=exec_train_model).pack(pady=10)
tk.Button(window, text="Recognize Gestures", command=exec_gesture_recognition).pack(pady=10)

# Iniciar janela
window.mainloop()
