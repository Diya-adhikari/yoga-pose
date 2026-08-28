#  YogaPoseClassifier

**YogaPoseClassifier is a machine learning project built with **MediaPipe** and Python to classify yoga poses using landmark extraction and angle-based features**

---
##  Features
- Real-time yoga pose detection with **MediaPipe**  
- Angle-based landmark extraction for robust classification  
- Modular training and prediction scripts for flexibility  
- Pre-trained models included for quick testing  

---

##  Tech Stack
- **Python 3.x**  
- **MediaPipe**  
- **Scikit-learn**  
- **OpenCV**
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
## Features
- Real-time yoga pose detection with MediaPipe.
- Angle-based landmark extraction for robust classification.
- Modular training and prediction scripts.
- Pre-trained models included for quick testing.
