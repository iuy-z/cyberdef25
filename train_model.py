import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# 10-sample realistic dataset
data = {
    "bytes_in":  [50,120,300,500,50,2000,1500,80,900,4000],
    "bytes_out": [40,100,250,450,20,1800,1400,60,850,3900],
    "packets":   [10,25,60,80,5,300,250,12,150,500],
    "duration":  [1,2,5,8,1,20,15,2,10,30],
    "label":     [0,0,0,1,0,1,1,0,1,1]     # 1 = malicious
}

df = pd.DataFrame(data)
X = df[["bytes_in","bytes_out","packets","duration"]]
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl has been created successfully!")
