import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from data_preprocessing import load_data, clean_data

# Load data
df = load_data()
df = clean_data(df)

# Feature engineering
df["lag_1"] = df["Sales"].shift(1)
df["lag_2"] = df["Sales"].shift(2)
df["rolling_mean"] = df["Sales"].rolling(3).mean()

df = df.dropna()

# Features & target
X = df[["lag_1", "lag_2", "rolling_mean"]]
y = df["Sales"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model (simplified for stability)
model = RandomForestRegressor(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Plot results
plt.figure(figsize=(8,5))
plt.plot(y_test.values, label="Actual Sales")
plt.plot(y_pred, label="Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.legend()
plt.show()

print("Model trained successfully!")