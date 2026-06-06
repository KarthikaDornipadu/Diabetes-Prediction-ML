import pandas as pd

from preprocessing import preprocess_data
from feature_engineering import create_features

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from xgboost import XGBClassifier

# Load Dataset
df = pd.read_csv("dataset.csv")

# Preprocess
df = preprocess_data(df)

# Feature Engineering
df = create_features(df)

# Split Features and Target
X = df.drop("diabetes", axis=1)
y = df["diabetes"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Base Models
estimators = [
    ("rf", RandomForestClassifier()),
    ("xgb", XGBClassifier(eval_metric="logloss"))
]

# Stacking Model
model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)

# Train
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, pred)

print("Accuracy :", accuracy)

print("\nClassification Report\n")
print(classification_report(y_test, pred))