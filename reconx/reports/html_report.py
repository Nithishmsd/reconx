from datetime import datetime

def generate_html_report(target, results, output_file):
    html = f"""
    <html>
    <head>
        <title>ReconX Report - {target}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #0f172a;
                color: #e5e7eb;
                padding: 20px;
            }}
            h1, h2 {{
                color: #38bdf8;
            }}
            .section {{
                background: #020617;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 8px;
            }}
            pre {{
                white-space: pre-wrap;
                word-wrap: break-word;
                background: #020617;
                padding: 10px;
                border-radius: 5px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #334155;
                padding: 8px;
            }}
            th {{
                background-color: #1e293b;
            }}
        </style>
    </head>
    <body>

    <h1>ReconX Reconnaissance Report</h1>
    <p><strong>Target:</strong> {target}</p>
    <p><strong>Date:</strong> {datetime.now()}</p>
    """

    # WHOIS
    if "whois" in results:
        html += f"""
        <div class="section">
            <h2>WHOIS Information</h2>
            <pre>{results["whois"]}</pre>
        </div>
        """

    # Subdomains
    if "subdomains" in results:
        html += """
        <div class="section">
            <h2>Subdomains</h2>
            <ul>
        """
        for sub in results["subdomains"]:
            html += f"<li>{sub}</li>"
        html += "</ul></div>"

    # Network
    if "network" in results:
        html += """
        <div class="section">
            <h2>Network Services</h2>
            <table>
                <tr>
                    <th>Port</th>
                    <th>Protocol</th>
                    <th>Service</th>
                    <th>Product</th>
                    <th>Version</th>
                </tr>
        """
        for svc in results["network"]:
            html += f"""
            <tr>
                <td>{svc.get("port")}</td>
                <td>{svc.get("protocol")}</td>
                <td>{svc.get("service")}</td>
                <td>{svc.get("product")}</td>
                <td>{svc.get("version")}</td>
            </tr>
            """
        html += "</table></div>"

    # Web
    if "web" in results:
        html += """
        <div class="section">
            <h2>Web Recon</h2>
            <table>
                <tr>
                    <th>URL</th>
                    <th>Status</th>
                    <th>Title</th>
                    <th>Server</th>
                    <th>Technologies</th>
                </tr>
        """
        for site in results["web"]:
            html += f"""
            <tr>
                <td>{site.get("url")}</td>
                <td>{site.get("status_code")}</td>
                <td>{site.get("title")}</td>
                <td>{site.get("webserver")}</td>
                <td>{", ".join(site.get("technologies", []))}</td>
            </tr>
            """
        html += "</table></div>"

    html += "</body></html>"

    with open(output_file, "w") as f:
        f.write(html)
