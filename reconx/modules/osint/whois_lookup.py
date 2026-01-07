import subprocess
from reconx.core.utils import opsec_delay

def run_whois(target):
    print("[*] Running WHOIS lookup...")
    opsec_delay()

    try:
        result = subprocess.run(
            ["whois", target],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout
    except Exception as e:
        return f"WHOIS failed: {str(e)}"

