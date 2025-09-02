# predict_binary.py
import sys, numpy as np, joblib, pathlib

MODEL = r"C:\ai-antivirus\malimg_binary_rf_model.pkl"

def file_to_32x32(path):
    with open(path, "rb") as f:
        b = f.read(1024)
    arr = np.frombuffer(b, dtype=np.uint8)
    if arr.size < 1024:
        arr = np.pad(arr, (0, 1024 - arr.size))
    return arr.reshape(32, 32)

clf = joblib.load(MODEL)
print("✅ Model loaded.")

path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Windows\System32\notepad.exe"
x = file_to_32x32(path).reshape(1, -1)
prob = clf.predict_proba(x)[0][1]  # prob(malware)
label = int(prob >= 0.60)          # threshold 0.60 (tune later)
print(f"🎯 Path: {path}")
print(f"   Malware probability: {prob:.3f}  ->  Pred: {'MALWARE' if label else 'BENIGN'}")
