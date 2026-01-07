import shutil
import sys

def check_tool(tool_name):
    if not shutil.which(tool_name):
        print(f"[!] Required tool not found: {tool_name}")
        print("[!] Please install it and try again.")
        sys.exit(1)
