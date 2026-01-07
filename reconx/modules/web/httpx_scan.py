import subprocess
import json
from reconx.core.utils import check_tool, opsec_delay

def run_web_recon(target):
    print("[*] Running web reconnaissance...")
    check_tool("httpx")
    opsec_delay()

    try:
        result = subprocess.run(
            [
                "httpx",
                "-silent",
                "-tech-detect",
                "-json",
                "-u", target
            ],
            capture_output=True,
            text=True,
            timeout=120
        )

        findings = []
        for line in result.stdout.splitlines():
            try:
                data = json.loads(line)
                findings.append({
                    "url": data.get("url"),
                    "status_code": data.get("status_code"),
                    "title": data.get("title"),
                    "webserver": data.get("webserver"),
                    "technologies": data.get("tech", [])
                })
            except Exception:
                pass

        return findings

    except Exception as e:
        return {"error": str(e)}
