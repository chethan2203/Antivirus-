🛡️ AI Antivirus

An experimental AI-powered antivirus that uses machine learning to classify files as benign or malicious by monitoring a folder in real-time.

✅ Features (Completed So Far)

File Monitoring

Watches the incoming/ directory for new files.

Scans all file types (.exe, .pdf, .txt, .docx, images, etc.).

Static Analysis (ML-based)

Converts file bytes into a fixed 32×32 representation.

Uses a trained Random Forest classifier (malimg_binary_rf_model.pkl).

Produces a malware probability score.

Quarantine System

If malware is detected, file is automatically moved to the quarantine/ folder.

Keeps the system safe while preserving suspicious files.

Logging

Each scan prints probability score + decision (BENIGN / MALWARE).

Example output:

[2025-09-02 11:31:35] resume.txt → prob=0.787 → MALWARE  
⚠️ Quarantined → C:\ai-antivirus\quarantine\resume.txt# Antivirus-
