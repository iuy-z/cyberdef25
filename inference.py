import pandas as pd
import pickle
import os

MODEL_PATH = "model.pkl"
INPUT_DIR = "/input/logs"
OUTPUT_PATH = "/output/alerts.csv"

# Load model
model = pickle.load(open(MODEL_PATH, "rb"))

# Read logs
files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".log") or f.endswith(".csv")]

alerts = []

for file in files:
    df = pd.read_csv(os.path.join(INPUT_DIR, file))
    predictions = model.predict(df)

    for i, pred in enumerate(predictions):
        if pred == 1:
            alerts.append({"file": file, "row": i, "alert": "Malicious activity detected"})

alerts_df = pd.DataFrame(alerts)
alerts_df.to_csv(OUTPUT_PATH, index=False)
print("Analysis complete! Alerts saved.")
