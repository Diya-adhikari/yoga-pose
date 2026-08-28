# extract_landmarks_with_angles.py

import cv2
import mediapipe as mp
import os
import csv
from pose_utils import calculateAngle

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

# Paths
DATASET_PATH = "dataset"
SAVE_PATH = "data"

# Create save directory if it doesn't exist
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# Loop through each pose folder
for pose_name in os.listdir(DATASET_PATH):
    folder_path = os.path.join(DATASET_PATH, pose_name)
    save_file = os.path.join(SAVE_PATH, f"{pose_name}.csv")

    with open(save_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header: 33 landmarks × 3 coords + 3 angles + label
        header = [f"{i}_{coord}" for i in range(33) for coord in ['x', 'y', 'z']]
        header += ['left_elbow_angle', 'right_elbow_angle', 'left_knee_angle', 'label']
        writer.writerow(header)

        # Loop through images
        for img_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img_name)
            image = cv2.imread(img_path)
            if image is None:
                continue

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = pose.process(image_rgb)

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                row = []

                # Save coordinates
                for lm in landmarks:
                    row.extend([lm.x, lm.y, lm.z])

                # Define landmark indices
                LEFT_SHOULDER = 11
                LEFT_ELBOW = 13
                LEFT_WRIST = 15
                RIGHT_SHOULDER = 12
                RIGHT_ELBOW = 14
                RIGHT_WRIST = 16
                LEFT_HIP = 23
                LEFT_KNEE = 25
                LEFT_ANKLE = 27

                # Calculate angles
                left_elbow_angle = calculateAngle(
                    (landmarks[LEFT_SHOULDER].x, landmarks[LEFT_SHOULDER].y, landmarks[LEFT_SHOULDER].z),
                    (landmarks[LEFT_ELBOW].x, landmarks[LEFT_ELBOW].y, landmarks[LEFT_ELBOW].z),
                    (landmarks[LEFT_WRIST].x, landmarks[LEFT_WRIST].y, landmarks[LEFT_WRIST].z)
                )

                right_elbow_angle = calculateAngle(
                    (landmarks[RIGHT_SHOULDER].x, landmarks[RIGHT_SHOULDER].y, landmarks[RIGHT_SHOULDER].z),
                    (landmarks[RIGHT_ELBOW].x, landmarks[RIGHT_ELBOW].y, landmarks[RIGHT_ELBOW].z),
                    (landmarks[RIGHT_WRIST].x, landmarks[RIGHT_WRIST].y, landmarks[RIGHT_WRIST].z)
                )

                left_knee_angle = calculateAngle(
                    (landmarks[LEFT_HIP].x, landmarks[LEFT_HIP].y, landmarks[LEFT_HIP].z),
                    (landmarks[LEFT_KNEE].x, landmarks[LEFT_KNEE].y, landmarks[LEFT_KNEE].z),
                    (landmarks[LEFT_ANKLE].x, landmarks[LEFT_ANKLE].y, landmarks[LEFT_ANKLE].z)
                )

                # Add angles and label
                row.extend([left_elbow_angle, right_elbow_angle, left_knee_angle])
                row.append(pose_name)

                # Write to CSV
                writer.writerow(row)