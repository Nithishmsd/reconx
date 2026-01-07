import shutil
import sys
import time
import random

def check_tool(tool):
    if not shutil.which(tool):
        print(f"[!] Missing required tool: {tool}")
        print("[!] Install it and retry")
        sys.exit(1)

def opsec_delay(min_sec=1, max_sec=3):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

