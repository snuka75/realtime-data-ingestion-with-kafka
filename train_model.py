import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import joblib
import json

# Load data
df = pd.read_csv("UNSW_NB15_training-set.csv")

# Drop unnecessary columns
df = df.drop(columns=["attack_cat", "id"], errors="ignore")

# Identify categorical columns
cat_cols = df.select_dtypes(include="object").columns

# Apply label encoding
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col].astype(str))

# Split features and labels
X = df.drop("label", axis=1)
y = df["label"]

# ✅ Print and save feature columns used for training
feature_columns = X.columns.tolist()
print("✅ Feature columns used in training:")
print(feature_columns)

# Save the feature list to JSON (for Spark stream to use)
with open("features.json", "w") as f:
    json.dump(feature_columns, f)

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "rf_model.pkl")
print("✅ Model trained and saved as rf_model.pkl")

# Evaluate
print("\n📊 Classification Report:")
print(classification_report(y_test, model.predict(X_test)))
