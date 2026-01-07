from reconx.modules.osint.whois_lookup import run_whois

class ReconEngine:
    def __init__(self, target):
        self.target = target
        self.results = {}

    def run_osint(self):
        print("[*] Running OSINT modules...")
        whois_data = run_whois(self.target)
        self.results["whois"] = whois_data

    def run(self, args):
        if args.osint:
            self.run_osint()

        return self.results
