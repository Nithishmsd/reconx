from reconx.modules.osint.whois_lookup import run_whois
from reconx.modules.osint.subdomains import run_subdomain_enum
from reconx.modules.network.nmap_scan import run_nmap
from reconx.modules.web.httpx_scan import run_web_recon

class ReconEngine:
    def __init__(self, target):
        self.target = target
        self.results = {}

    def run_osint(self):
        print("[*] Running OSINT modules...")
        self.results["whois"] = run_whois(self.target)
        self.results["subdomains"] = run_subdomain_enum(self.target)

    def run_network(self):
        print("[*] Running Network Recon...")
        self.results["network"] = run_nmap(self.target)

    def run_web(self):
        print("[*] Running Web Recon...")
        self.results["web"] = run_web_recon(self.target)

    def run(self, args):
        if args.osint:
            self.run_osint()

        if args.network:
            self.run_network()

        if args.web:
            self.run_web()

        return self.results

