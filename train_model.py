import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

data_path = "data"
all_data = []

for file in os.listdir(data_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(data_path, file))
        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)
X = combined_df.drop("label", axis=1)
y = combined_df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

if not os.path.exists("model"):
    os.makedirs("model")

with open("model/yoga_pose_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")