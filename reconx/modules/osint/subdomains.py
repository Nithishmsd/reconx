import subprocess
from reconx.core.utils import check_tool, opsec_delay

def run_subdomain_enum(target):
    print("[*] Running subdomain enumeration...")
    subdomains = set()

    check_tool("subfinder")
    opsec_delay()

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

    check_tool("amass")
    opsec_delay()

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

