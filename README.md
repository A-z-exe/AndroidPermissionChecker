# 🛡️ Android Permission Checker
Educational CLI tool for analyzing Android app permissions from AndroidManifest.xml files. Helps understand privacy risks by detecting dangerous permissions and calculating a simple risk score.

## ⚠️ Legal & Ethical Disclaimer
**IMPORTANT**: This tool is strictly for **educational, research, and ethical purposes** only. Users must:
- Only analyze apps you own, develop yourself, or have explicit permission to examine
- Use only on decompiled files from legitimate sources (e.g., your own APKs, open-source samples)
- Comply with all privacy laws, data protection regulations, and platform policies
- Never use findings for malicious, unauthorized, or illegal activities

Analyzing permissions without authorization may violate terms of service or laws.  
**You are solely responsible** for legal and ethical compliance. The author assumes no liability.

## 🚀 Features
- Extracts all declared permissions (`<uses-permission>`) from AndroidManifest.xml
- Classifies permissions as **Normal** vs **Dangerous** (based on official Android documentation)
- Calculates a basic **risk score** (0–100) based on dangerous permissions count
- Supports output in **plain text** or **JSON** (easy for automation & scripting)
- Zero external dependencies – pure Python standard library
- Works on Linux, Windows, macOS, Termux, Kali – anywhere Python 3 runs

## 📋 Requirements
- Python 3.6 or higher (no pip packages needed!)
- AndroidManifest.xml file (extracted from APK using tools like `apktool`, `aapt`, `jadx`, etc.)

## 🔧 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/a-z-exe/AndroidPermissionChecker.git
   cd AndroidPermissionChecker
