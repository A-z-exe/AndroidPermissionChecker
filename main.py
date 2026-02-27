#!/usr/bin/env python3
"""
AndroidPermissionChecker - Educational tool for static analysis of Android app permissions

Analyzes AndroidManifest.xml to extract and classify permissions,
highlighting dangerous ones and computing a weighted risk score.

Author: AmirHossein Zarei (GitHub: a-z-exe)
License: MIT
Disclaimer: For educational and authorized research use only.
Misuse is solely the user's responsibility.
"""

import argparse
import json
import logging
import sys
from collections import Counter
from typing import Dict, List, Any
import xml.etree.ElementTree as ET

# ────────────────────────────────────────────────
#     رنگ‌ها (نیاز به نصب colorama دارد)
# ────────────────────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)  # برای ویندوز و ترمینال‌های مختلف
except ImportError:
    # اگر colorama نصب نبود → رنگ‌ها خاموش
    class DummyColor:
        YELLOW = ''
        GREEN  = ''
        CYAN   = ''
        RESET_ALL = ''
    Fore = DummyColor()
    Style = DummyColor()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

# Android XML namespace
ANDROID_NS = 'http://schemas.android.com/apk/res/android'
NS = {'android': ANDROID_NS}

# Dangerous permissions with approximate weights
DANGEROUS_PERMS: Dict[str, int] = {
    'android.permission.ACCESS_FINE_LOCATION': 20,
    'android.permission.ACCESS_COARSE_LOCATION': 15,
    'android.permission.ACCESS_BACKGROUND_LOCATION': 25,
    'android.permission.CAMERA': 20,
    'android.permission.RECORD_AUDIO': 20,
    'android.permission.READ_CONTACTS': 15,
    'android.permission.READ_CALENDAR': 12,
    'android.permission.READ_CALL_LOG': 15,
    'android.permission.READ_SMS': 25,
    'android.permission.RECEIVE_SMS': 20,
    'android.permission.SEND_SMS': 20,
    'android.permission.READ_PHONE_STATE': 18,
    'android.permission.READ_EXTERNAL_STORAGE': 8,
    'android.permission.WRITE_EXTERNAL_STORAGE': 8,
    # می‌تونی موارد دیگه رو اضافه کنی
}

def print_banner():
    banner = f"""
{Fore.CYAN}    ╔════════════════════════════════════════════╗
{Fore.CYAN}    ║                                            ║
{Fore.CYAN}    ║                  APC 🔎                    ║
{Fore.CYAN}    ║     Android Permission Checker             ║
{Fore.CYAN}    ║                                            ║
{Fore.CYAN}    ║  {Fore.GREEN}v1.0{Style.RESET_ALL}      Educational Tool            ║
{Fore.CYAN}    ║                                            ║
{Fore.CYAN}    ║  {Fore.YELLOW}For Educational Purposes Only{Style.RESET_ALL}         ║
{Fore.CYAN}    ║                                            ║
{Fore.CYAN}    ║  GitHub    → github.com/a-z-exe            ║
{Fore.CYAN}    ║  Telegram  → t.me/A_Z_exe                  ║
{Fore.CYAN}    ╚════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)
    print(Style.RESET_ALL)
def extract_permissions(xml_path: str) -> List[str]:
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        permissions: List[str] = []

        for elem in root.iterfind('.//uses-permission'):
            name = elem.get(f'{{{ANDROID_NS}}}name')
            if name:
                permissions.append(name)

        for elem in root.iterfind('.//uses-permission-sdk-23'):
            name = elem.get(f'{{{ANDROID_NS}}}name')
            if name:
                permissions.append(name)

        return list(set(permissions))

    except ET.ParseError as e:
        logger.error("Failed to parse XML: %s", e)
        sys.exit(2)
    except FileNotFoundError:
        logger.error("File not found: %s", xml_path)
        sys.exit(2)
    except Exception as e:
        logger.exception("Unexpected error")
        sys.exit(3)


def analyze_permissions(permissions: List[str]) -> Dict[str, Any]:
    all_perms = Counter(permissions)
    dangerous_found: List[str] = []
    total_risk = 0

    for perm in permissions:
        if perm in DANGEROUS_PERMS:
            dangerous_found.append(perm)
            total_risk += DANGEROUS_PERMS[perm]

    normal = [p for p in permissions if p not in DANGEROUS_PERMS]

    risk_score = min(total_risk, 100)
    if risk_score < 30:
        level = "Low"
    elif risk_score < 70:
        level = "Medium"
    else:
        level = "High"

    return {
        'total_permissions': len(permissions),
        'normal_permissions': len(normal),
        'dangerous_permissions': len(dangerous_found),
        'risk_score': risk_score,
        'risk_level': level,
        'all_permissions': dict(all_perms),
        'dangerous_list': sorted(dangerous_found),
        'normal_list': sorted(normal)
    }


def print_text_report(analysis: Dict[str, Any]) -> None:
    print("═" * 45)
    print(" Android Permission Analysis Report ")
    print("═" * 45)
    print(f"Total Permissions     : {analysis['total_permissions']}")
    print(f"Normal Permissions    : {analysis['normal_permissions']}")
    print(f"Dangerous Permissions : {analysis['dangerous_permissions']}")
    print(f"Risk Score            : {analysis['risk_score']}/100  →  {analysis['risk_level']}")
    print("═" * 45)

    if analysis['dangerous_permissions'] > 0:
        print(f"{Fore.YELLOW}Dangerous Permissions:{Style.RESET_ALL}")
        for p in analysis['dangerous_list']:
            w = DANGEROUS_PERMS.get(p, 0)
            print(f"  - {p:<55}  weight: {w}")
    else:
        print(f"{Fore.GREEN}No dangerous permissions detected.{Style.RESET_ALL}")

    print("\nNormal Permissions:")
    for p in analysis['normal_list']:
        print(f"  - {p}")
    print("═" * 45)


def main() -> None:
    print_banner()   # ← بنر اینجا نمایش داده می‌شود

    parser = argparse.ArgumentParser(
        description='Educational Android Permission Analyzer'
    )
    parser.add_argument('xml_file', type=str, help='Path to AndroidManifest.xml')
    parser.add_argument('-o', '--output', choices=['text', 'json'], default='text',
                        help='Output format (default: text)')

    args = parser.parse_args()

    logger.info("Analyzing: %s", args.xml_file)

    perms = extract_permissions(args.xml_file)
    analysis = analyze_permissions(perms)

    if args.output == 'json':
        print(json.dumps(analysis, indent=2, sort_keys=True))
    else:
        print_text_report(analysis)

    # Exit code بر اساس ریسک
    if analysis['risk_score'] >= 70:
        sys.exit(10)
    elif analysis['risk_score'] >= 30:
        sys.exit(5)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()