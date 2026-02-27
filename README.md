# 🛡️ Android Permission Checker

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)
![Focus](https://img.shields.io/badge/Focus-Mobile%20Security-red)

> Educational CLI tool for static analysis of Android application
> permissions.\
> Designed for learning Android security, privacy auditing, and
> permission risk modeling.

------------------------------------------------------------------------

## 📌 Overview

Android Permission Checker is a lightweight Python-based CLI tool that:

-   Extracts permissions from `AndroidManifest.xml`
-   Identifies dangerous permissions
-   Calculates a simple privacy risk score
-   Provides output in text or JSON format
-   Works fully offline

This project demonstrates:

-   Android permission model understanding
-   Static analysis concepts
-   Risk scoring logic
-   CLI tool development
-   Secure & ethical software design principles

------------------------------------------------------------------------

## ⚠️ Legal & Ethical Disclaimer

This project is strictly for **educational and research purposes**.

You must:

-   Analyze only apps you own or have permission to inspect\
-   Use legally obtained APK files\
-   Respect privacy laws and digital regulations

The author assumes no responsibility for misuse.

------------------------------------------------------------------------

## 🚀 Features

-   ✅ Parses `uses-permission`
-   ✅ Parses `uses-permission-sdk-23`
-   ✅ Detects known dangerous permissions
-   ✅ Calculates capped risk score (0--100)
-   ✅ Risk classification (Low / Medium / High)
-   ✅ JSON export for automation
-   ✅ No third‑party dependencies

------------------------------------------------------------------------

## 📂 Project Structure

    AndroidPermissionChecker/
    │
    ├── main.py
    ├── README.md
    └── LICENSE

------------------------------------------------------------------------

## 🔧 Installation

``` bash
git clone https://github.com/A-z-exe/AndroidPermissionChecker.git
cd AndroidPermissionChecker
chmod +x main.py   # Optional (Linux/macOS)
```

------------------------------------------------------------------------

## 💻 Usage

### Basic Analysis

``` bash
python main.py path/to/AndroidManifest.xml
```

### JSON Output

``` bash
python main.py path/to/AndroidManifest.xml -o json
```

### Help

``` bash
python main.py --help
```

------------------------------------------------------------------------

## 📊 Example Output

    === Android Permission Analysis ===
    Total Permissions: 12
    Normal: 8
    Dangerous: 4
    Risk Score: 40/100 (Medium Risk)

------------------------------------------------------------------------

## 🔎 Risk Scoring Model

-   Each dangerous permission = 10 points\
-   Score capped at 100\
-   Risk classification:
    -   0--29 → Low
    -   30--59 → Medium
    -   60--100 → High

This scoring model is intentionally simple for educational clarity.

------------------------------------------------------------------------

## 🧠 Technical Highlights

-   XML parsing via `xml.etree.ElementTree`
-   Argument handling with `argparse`
-   Data aggregation using `collections.Counter`
-   Modular function design
-   CLI automation support

------------------------------------------------------------------------

## 📈 Roadmap

-   [ ] Support direct APK analysis (auto-extract manifest)
-   [ ] Integrate Android permission groups
-   [ ] Export HTML security report
-   [ ] Add severity weighting system
-   [ ] Add GitHub Actions CI
-   [ ] Add unit tests with pytest

------------------------------------------------------------------------

## 🤝 Contributing

1.  Fork the repository\
2.  Create a feature branch\
3.  Commit changes\
4.  Submit a Pull Request

Please follow PEP 8 standards.

------------------------------------------------------------------------

## ⚖️ License

MIT License

------------------------------------------------------------------------

## 👨‍💻 Author

**AmirHossein Zarei (A-z-exe)**\
Security Enthusiast \| Future White‑Hat\
GitHub: https://github.com/A-z-exe\
Telegram: https://t.me/A_Z\_exe
