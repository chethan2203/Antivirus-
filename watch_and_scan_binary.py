# watch_and_scan_binary.py
import os, time, shutil, numpy as np, joblib, pathlib

WATCH = r"C:\ai-antivirus\incoming"
QUAR  = r"C:\ai-antivirus\quarantine"
MODEL = r"C:\ai-antivirus\malimg_binary_rf_model.pkl"
THRESH = 0.60

def file_to_32x32(path):
    with open(path, "rb") as f:
        b = f.read(1024)
    arr = np.frombuffer(b, dtype=np.uint8)
    if arr.size < 1024:
        arr = np.pad(arr, (0, 1024 - arr.size))
    return arr.reshape(32, 32)

clf = joblib.load(MODEL)
print(f"✅ Model loaded. Watching: {WATCH}")

seen = set()
pathlib.Path(QUAR).mkdir(parents=True, exist_ok=True)
pathlib.Path(WATCH).mkdir(parents=True, exist_ok=True)

while True:
    for p in pathlib.Path(WATCH).glob("*"):
        if p.is_file() and p not in seen:
            seen.add(p)
            try:
                x = file_to_32x32(str(p)).reshape(1, -1)
                prob = clf.predict_proba(x)[0][1]
                is_mal = prob >= THRESH
                ts = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{ts}] {p.name} → prob={prob:.3f} → {'MALWARE' if is_mal else 'BENIGN'}")
                if is_mal:
                    dest = pathlib.Path(QUAR) / p.name
                    shutil.move(str(p), str(dest))
                    print(f"⚠️  Quarantined → {dest}")
            except Exception as e:
                print(f"ERR {p.name}: {e}")
    time.sleep(1)
