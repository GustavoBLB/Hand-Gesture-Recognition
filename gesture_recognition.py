import cv2
import mediapipe as mp
import joblib
import numpy as np
import pandas as pd

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

model = joblib.load("model.pkl")

column_names = []
for i in range(1, 22):
    column_names.append(f'{i}x')
    column_names.append(f'{i}y')
    column_names.append(f'{i}z')

while True:
    ret, frame = camera.read()

    if not ret:
        print("Error capturing image.")
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )

            list_data = []
            x_wrist = hand_landmarks.landmark[0].x
            y_wrist = hand_landmarks.landmark[0].y
            z_wrist = hand_landmarks.landmark[0].z

            for id_point ,landmark in enumerate(hand_landmarks.landmark):        
                list_data.append(landmark.x - x_wrist)
                list_data.append(landmark.y - y_wrist)
                list_data.append(landmark.z - z_wrist)

            input_df = pd.DataFrame([list_data], columns=column_names)

            if len(list_data) == 63:

                probs = model.predict_proba(input_df)
                max_prob = np.max(probs)

                if max_prob < 0.9:  
                    label_value = "unknown"
                else:
                    label_value = model.predict(input_df)[0]

                landmark = hand_landmarks.landmark[0]

                h, w, _ = frame.shape
                x = int(landmark.x * w)
                y = int(landmark.y * h)

                cv2.putText(frame,
                            str(label_value), 
                            (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            1, 
                            (0, 255, 0), 
                            2, 
                            cv2.LINE_AA)

    cv2.imshow(f"Camera - Press 'q' to leave", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
