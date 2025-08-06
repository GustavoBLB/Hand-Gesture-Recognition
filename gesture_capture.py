import cv2
import mediapipe as mp
import csv
import os
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()


file_csv_name = 'database.csv'

file_exists = os.path.exists(file_csv_name)

if not file_exists:
    with open(file_csv_name , mode='w', newline='') as acrchive:
        writer_csv = csv.writer(acrchive)
        label = ['label']
        for i in range(1 , 22):
            label.append(f'{i}x')
            label.append(f'{i}y')
            label.append(f'{i}z')
        writer_csv.writerow(label)

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not camera.isOpened():
    print(f"Error: Unable to access the camera.")
    exit()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,       
    max_num_hands=1,                
    min_detection_confidence=0.7    
)


def saving_gesture(file_csv_name, hand_landmarks , label):

    if not label:
        print("No label entered.")
        return

    list_insert = [label]

    # Referência no punho
    x_wrist = hand_landmarks.landmark[0].x
    y_wrist = hand_landmarks.landmark[0].y
    z_wrist = hand_landmarks.landmark[0].z

    for landmark in hand_landmarks.landmark:
        list_insert.append(landmark.x - x_wrist)
        list_insert.append(landmark.y - y_wrist)
        list_insert.append(landmark.z - z_wrist)

    with open(file_csv_name, mode='a', newline='') as file:
        writer_csv = csv.writer(file)
        writer_csv.writerow(list_insert)

    print(f"Saving of [{label}] completed successfully.")

bit_multi_saving = 0
label = None

while True:

    ret, frame = camera.read()

    if not ret:
        print("Error capturing image.")
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('m'):
        label = simpledialog.askstring("Input", "Type what you are going to refer:")

        if label:  
            messagebox.showinfo("Multi-saving mode",
            f"Label: [{label}]\n\nPress 'S' to save\nPress 'L' to leave")
            bit_multi_saving = 1

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )

            if bit_multi_saving == 1:
                if key == ord('s'):
                    saving_gesture(file_csv_name, hand_landmarks , label)
            else:
                if key == ord('s'):
                    label = simpledialog.askstring("Input", "Type what you are referring to:")
                    saving_gesture(file_csv_name, hand_landmarks , label)

    if bit_multi_saving == 1 and key == ord('l'):
        bit_multi_saving = 0
        print('teste')

    if bit_multi_saving == 1 and label:
        cv2.putText(frame, 
            f"Multi-saving [{label}]",
            (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, 
            (0, 255, 0), 
            2)

        cv2.putText(frame, 
            "Press 'S' to save", 
            (10, 65), 
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5, 
            (0, 255, 255), 
            2)

        cv2.putText(frame, 
            "Press 'L' to leave", 
            (10, 100), 
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5, 
            (0, 255, 255), 
            2)



    cv2.imshow(f"Camera - Press 'q' to leave or 's' to save or 'm' for multi-saving", frame)

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
hands.close()
