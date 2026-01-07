import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="ReconX - Advanced Red Team Recon Automation Toolkit"
    )

    parser.add_argument("target", help="Target domain or IP address")
    parser.add_argument("--osint", action="store_true", help="Run OSINT recon")
    parser.add_argument("--network", action="store_true", help="Run network recon")
    parser.add_argument("--web", action="store_true", help="Run web recon")
    parser.add_argument("--legal", action="store_true", help="Accept legal disclaimer")

    args = parser.parse_args()

    if not args.legal:
        print("[!] You must accept the legal disclaimer using --legal")
        sys.exit(1)

    print("[+] ReconX started")
    print(f"[+] Target : {args.target}")
    print(f"[+] OSINT  : {args.osint}")
    print(f"[+] Network: {args.network}")
    print(f"[+] Web    : {args.web}")
