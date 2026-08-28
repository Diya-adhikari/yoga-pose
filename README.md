#  YogaPoseClassifier

**YogaPoseClassifier is a machine learning project built with **MediaPipe** and Python to classify yoga poses using landmark extraction and angle-based features**

---
##  Features
- Real-time yoga pose detection with **MediaPipe**  
- Angle-based landmark extraction for robust classification  
- Modular training and prediction scripts for flexibility  
- Pre-trained models included for quick testing  

---

## 📊 Tech Stack

- **Programming Language**
  - Python

- **Computer Vision**
  - OpenCV (`cv2`)
  - MediaPipe (`mediapipe`)

- **Machine Learning**
  - Scikit-learn (`RandomForestClassifier`, `train_test_split`, `classification_report`)
  - Joblib (`joblib`) for model persistence
  - Pickle (`pickle`) for saving/loading models

- **Data Handling**
  - NumPy (`numpy`)
  - Pandas (`pandas`)
  - CSV (`csv`)

- **Utilities**
  - OS (`os`) for file handling
  - Time (`time`) for performance measurement
  - Custom utilities (`pose_utils.calculateAngle`)

---

## 🧩 Features
- Real-time yoga pose detection with **MediaPipe**  
- Angle-based landmark extraction for robust classification  
- Modular training and prediction scripts  
- Pre-trained models included for quick testing  

---
##  Project Structure

- **data/**  
  - Stores raw yoga pose data.

- **dataset/**  
  - Contains processed datasets used for training and testing.

- **mediapipe-env/**  
  - Python virtual environment for the project.  
  - Includes:
    - `Include/` → Header files.  
    - `Lib/` → Libraries.  
    - `Scripts/` → Executable scripts.  
    - `pyvenv.cfg` → Virtual environment configuration.  
    - `requirements.txt` → List of dependencies.

- **model/**  
  - Core ML scripts and trained models.  
  - Files include:
    - `yoga_pose_model.pkl` → Trained yoga pose model.  
    - `pose_classifier.pkl` → Classifier for pose recognition.  
    - `extract_landmarks_with_angles.py` → Extracts landmarks and calculates angles.  
    - `pose_utils.py` → Utility functions for pose handling.  
    - `predict_pose.py` → Script to predict yoga poses.  
    - `test_webcam_pose.py` → Test yoga pose classification using webcam.  
    - `train_model.py` → Training pipeline for yoga pose model.  
    - `train_pose_classifier.py` → Training script for pose classifier.
    ---
    ---
<img width="1486" height="1053" alt="Screenshot 2025-08-17 162658" src="https://github.com/user-attachments/assets/fe13e172-8b51-466a-85ac-69e1aadebd6f" />
<img width="1523" height="1096" alt="Screenshot 2025-08-17 162810" src="https://github.com/user-attachments/assets/facf386f-87f0-4489-9894-33d9425e9855" />
<img width="2434" height="843" alt="Screenshot 2025-08-17 163446" src="https://github.com/user-attachments/assets/10660c4b-1d64-4a0e-8571-404415709e82" />
<img width="1832" height="1059" alt="Screenshot 2025-08-17 222627" src="https://github.com/user-attachments/assets/ab11636a-1aa8-4564-b1ff-bf78aaf8d613" />
<img width="2620" height="1452" alt="Screenshot 2025-08-17 225125" src="https://github.com/user-attachments/assets/e67c6518-fd23-41c1-96a3-aa7ce9c66bf2" />


