

## ReconX 🔴

Advanced Red Team Reconnaissance Automation Toolkit for Linux.

ReconX automates OSINT, network, and web reconnaissance with OPSEC-safe execution
and generates JSON and HTML reports



## Features
- OSINT Recon (WHOIS, Subdomain Enumeration)
- Network Recon (Nmap service detection)
- Web Recon (Live hosts & technology detection)
- OPSEC-safe execution
- JSON & HTML reports


## Installation

### Clone the Repository
```bash

git clone https://github.com/Nithishmsd/reconx.git
cd reconx


## Install Dependencies

sudo apt install -y nmap whois amass subfinder httpx
pip3 install -r requirements.txt

✔ This is **standard open-source practice**  
✔ Every GitHub user expects this section

---

## Usage Section

```md
## Usage


### Full Recon

```bash

python3 reconx.py example.com --osint --network --web --legal



### OSINT Only

python3 reconx.py example.com --osint --legal


---

## Output Section

## Output

Reports are generated in the `reports/` directory:
- JSON report
- HTML report (client-ready)







Legal Disclaimer  

## Disclaimer

This tool is intended for educational and authorized security testing only.
Unauthorized scanning is illegal.




