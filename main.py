import tkinter as tk
import subprocess
import sys
import threading

python_path = sys.executable

def run_script(script_name , action_description):

    for button in buttons:
        button.config(state='disabled')
    status_label.config(text=f"Currently {action_description}...")

    def run_archive():
        subprocess.run([python_path, script_name])
        window.after(0, restore_interface_state)

    threading.Thread(target=run_archive).start()

def restore_interface_state():
    for button in buttons:
        button.config(state='normal')
    status_label.config(text="Select an option below:")

window = tk.Tk()
window.title("Gesture Recognition Controller")
width_window = 400
height_window = 200

width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

pos_x = (width_screen // 2) - (width_window // 2)
pos_y = (height_screen // 2) - (height_window // 2)

window.geometry(f"{width_window}x{height_window}+{pos_x}+{pos_y}")

status_label = tk.Label(window, text='Select an option below:')
status_label.pack(pady=10)

buttons =   [
            tk.Button(window, text="Capture Gesture", command=lambda: run_script("gesture_capture.py" , "Capturing gesture")),
            tk.Button(window, text="Train Model", command=lambda: run_script("train_model.py" , "training model")),
            tk.Button(window, text="Recognize Gestures", command=lambda: run_script("gesture_recognition.py" , "recognition gesture"))
            ]

for button in buttons:
    button.pack(pady=5)

window.mainloop()
