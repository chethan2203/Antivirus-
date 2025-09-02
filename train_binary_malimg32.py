# train_binary_malimg32.py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

data = np.load(r"C:\ai-antivirus\datasets\binary_32x32.npz", allow_pickle=True)["arr"]

X = np.array([s[0] for s in data])          # 32x32 images (bytes view)
y = np.array([int(s[1]) for s in data])     # 0=benign, 1=malware

print("Total:", len(X), "| malware:", (y==1).sum(), "| benign:", (y==0).sum())
X = X.reshape(len(X), -1)                   # -> (N, 1024)

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

clf = RandomForestClassifier(n_estimators=300, max_features="sqrt", random_state=42, n_jobs=-1)
clf.fit(Xtr, ytr)

yp = clf.predict(Xte)
acc = accuracy_score(yte, yp)
print("\n🎯 Accuracy:", acc)
print("\n📊 Classification Report:")
print(classification_report(yte, yp, digits=4))

joblib.dump(clf, r"C:\ai-antivirus\malimg_binary_rf_model.pkl")
print("💾 Saved model -> C:\\ai-antivirus\\malimg_binary_rf_model.pkl")
