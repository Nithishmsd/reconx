import subprocess
import xml.etree.ElementTree as ET
from reconx.core.utils import check_tool, opsec_delay

def run_nmap(target):
    print("[*] Running Nmap scan...")
    check_tool("nmap")
    opsec_delay()

    output_file = f"/tmp/{target}_nmap.xml"

    try:
        subprocess.run(
            ["nmap", "-sV", "-oX", output_file, target],
            capture_output=True,
            text=True,
            timeout=300
        )
        return parse_nmap_xml(output_file)

    except Exception as e:
        return {"error": str(e)}

def parse_nmap_xml(xml_file):
    results = []

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for host in root.findall("host"):
        for port in host.findall(".//port"):
            state = port.find("state").attrib.get("state")
            if state != "open":
                continue

            service = port.find("service")
            results.append({
                "port": port.attrib.get("portid"),
                "protocol": port.attrib.get("protocol"),
                "service": service.attrib.get("name", ""),
                "product": service.attrib.get("product", ""),
                "version": service.attrib.get("version", "")
            })

    return results
