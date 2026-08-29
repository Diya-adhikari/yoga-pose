import cv2
import mediapipe as mp
import time
import joblib
import numpy as np
import pandas as pd  # Add this at the top

# Load the trained model
model = joblib.load("pose_classifier.pkl")

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# Initialize time for FPS calculation
prev_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    # Default label
    pose_label = "No Pose"

    # Draw pose landmarks and classify pose
    #   if results.pose_landmarks:
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Extract landmark coordinates
    landmarks = results.pose_landmarks.landmark
    features = []
    for lm in landmarks:
        features.extend([lm.x, lm.y, lm.z])

    # Create DataFrame with column names
    columns = [f"{axis}{i}" for i in range(33) for axis in ['x', 'y', 'z']]
    input_df = pd.DataFrame([features], columns=columns)

    # Predict pose label
    try:
        pose_label = model.predict(input_df)[0]
    except Exception as e:
        print("⚠️ Prediction error:", e)

    # Calculate FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Show predicted pose and FPS
    cv2.putText(frame, f"{pose_label} | FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Show the frame
    cv2.imshow("🧘‍♀️ Pose Detection", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()