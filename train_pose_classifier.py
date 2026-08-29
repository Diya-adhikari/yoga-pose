import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


# Load all CSVs from the data folder
data_dir = "data"
all_data = []

for file in os.listdir(data_dir):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(data_dir, file))
        all_data.append(df)

# Combine all pose data
full_df = pd.concat(all_data, ignore_index=True)

# Separate features and labels
X = full_df.drop("label", axis=1)
y = full_df["label"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
import joblib
joblib.dump(model, "pose_classifier.pkl")
