
# ReconX 🔴

**Red team reconnaissance automation toolkit for Linux.**

ReconX chains OSINT, network and web reconnaissance behind a single command, then writes the findings to both machine-readable JSON and a client-ready HTML report.

Reconnaissance is repetitive work: the same handful of tools, in the same order, with the results copy-pasted into a document by hand. ReconX automates that pipeline and makes the output consistent between engagements.

<!-- SCREENSHOT: replace this line with a terminal capture of a run, or a shot of the HTML report.
     Drag the image straight into the GitHub README editor and it uploads automatically. -->

---

## Modules

| Phase | Module | Tooling |
|---|---|---|
| **OSINT** | WHOIS lookup | `whois` |
| **OSINT** | Subdomain enumeration | `amass`, `subfinder` |
| **Network** | Port and service detection | `nmap` |
| **Web** | Live host and technology detection | `httpx` |

Each phase is opt-in via a flag, so you run only what the engagement scope permits.

---

## Architecture

```
reconx.py                 entry point
└── reconx/
    ├── cli.py            argparse, legal gate, report writing
    ├── engine.py         ReconEngine — orchestrates phases, collects results
    ├── config.py         settings
    ├── modules/
    │   ├── osint/        whois_lookup.py · subdomains.py
    │   ├── network/      nmap_scan.py
    │   └── web/          httpx_scan.py
    └── reports/          html_report.py
```

`ReconEngine` holds one results dictionary and each module contributes a key to it. Adding a new recon phase means writing one module and one `run_*` method — the CLI and both report formats pick it up without changes.

---

## Installation

```bash
git clone https://github.com/Nithishmsd/reconx.git
cd reconx

sudo apt install -y nmap whois amass subfinder httpx
pip3 install -r requirements.txt
```

## Usage

Full reconnaissance:
```bash
python3 reconx.py example.com --osint --network --web --legal
```

OSINT only:
```bash
python3 reconx.py example.com --osint --legal
```

Network scan only:
```bash
python3 reconx.py example.com --network --legal
```

| Flag | Effect |
|---|---|
| `--osint` | WHOIS + subdomain enumeration |
| `--network` | Nmap service detection |
| `--web` | Live host and technology detection |
| `--legal` | **Required.** Confirms you have authorisation to scan the target |

`--legal` is a deliberate hard gate: without it the tool exits before touching the target. Authorisation should be an explicit action, not an assumed default.

## Output

Two files per run, written to `reports/`:

```
reports/example.com_report.json    structured, for tooling and diffing
reports/example.com_report.html    formatted, for handing to a client
```

JSON keys map to the phases you ran — `whois`, `subdomains`, `network`, `web`.

---

## Known limitations

- **Depends on external binaries.** If `nmap`, `amass`, `subfinder` or `httpx` are missing from `PATH`, that module fails.
- **Phases run sequentially**, not in parallel — a full scan on a large target takes a while.
- **No resume.** An interrupted run starts over.
- **No rate limiting** beyond what the underlying tools apply themselves.

---

## Built with

Python 3 · argparse · nmap · amass · subfinder · httpx · whois

---

## What I learned

- **Orchestration is the hard part, not the scanning.** Every tool emits a different format; the real work is normalising them into one result structure that both reports can consume.
- **Designing for extensibility pays off immediately.** Because modules are isolated behind the engine, adding the web recon phase touched two files.
- **Safety rails belong in the interface.** The `--legal` flag makes authorisation a conscious step — a small design choice that reflects how scanning tools *should* be shipped.

---

## Disclaimer

This tool is for **educational use and authorised security testing only**. Scanning systems you do not own or have explicit written permission to test is illegal in most jurisdictions. See [DISCLAIMER.md](DISCLAIMER.md).
