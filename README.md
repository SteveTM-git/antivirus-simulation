# 🛡️ Basic Antivirus Simulation (Signature Based Scanner)

A Python based antivirus simulation that detects malicious files using SHA-256 hash comparison and isolates them using a quarantine mechanism.

---

## 🚀 Features

- 🔍 Recursive file scanning
- 🔐 SHA-256 hashing for file fingerprinting
- 🚨 Signature based malware detection
- 📦 Automatic quarantine of infected files
- 📜 Logging system for audit and traceability

---

## 📸 Photo

<img width="528" height="440" alt="image" src="https://github.com/user-attachments/assets/fb690e28-2468-4d8c-a86a-102774f5d307" />

---

## 🧠 How It Works

1. The scanner traverses a directory recursively.
2. Each file is hashed using SHA-256.
3. The hash is compared against a database of known malware signatures.
4. If a match is found:
   - The file is flagged as malicious
   - It is moved to a quarantine folder
   - The event is logged

---



