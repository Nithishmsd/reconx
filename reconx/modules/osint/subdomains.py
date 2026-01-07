import subprocess
from reconx.core.utils import check_tool

def run_subdomain_enum(target):
    print("[*] Running subdomain enumeration...")

    subdomains = set()

    # --- subfinder ---
    check_tool("subfinder")
    try:
        result = subprocess.run(
            ["subfinder", "-silent", "-d", target],
            capture_output=True,
            text=True,
            timeout=120
        )
        subdomains.update(result.stdout.splitlines())
    except Exception:
        pass

    # --- amass (passive) ---
    check_tool("amass")
    try:
        result = subprocess.run(
            ["amass", "enum", "-passive", "-d", target],
            capture_output=True,
            text=True,
            timeout=180
        )
        subdomains.update(result.stdout.splitlines())
    except Exception:
        pass

    return sorted(subdomains)
