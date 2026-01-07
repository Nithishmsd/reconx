import argparse
import sys
from reconx.engine import ReconEngine
import json
import os

def main():
    parser = argparse.ArgumentParser(
        description="ReconX - Advanced Red Team Recon Automation Toolkit"
    )

    parser.add_argument("target", help="Target domain or IP address")
    parser.add_argument("--osint", action="store_true", help="Run OSINT recon")
    parser.add_argument("--legal", action="store_true", help="Accept legal disclaimer")
    parser.add_argument("--network", action="store_true", help="Run network recon")
    parser.add_argument("--web", action="store_true", help="Run web reconnaissance")

    args = parser.parse_args()

    if not args.legal:
        print("[!] You must accept the legal disclaimer using --legal")
        sys.exit(1)

    engine = ReconEngine(args.target)
    results = engine.run(args)

    os.makedirs("reports", exist_ok=True)

    report_file = f"reports/{args.target}_report.json"
    with open(report_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"[+] Report saved to {report_file}")

