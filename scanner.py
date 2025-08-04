#!/usr/bin/env python3
#use virtualenv by running: python3 -m venv venv && source venv/bin/activate


import argparse, json, os, textwrap
from dotenv import load_dotenv
load_dotenv()
import nmap                                      #  pip install python-nmap
from openai import OpenAI                        # pip install openai>=1.0



# ---------- CLI ----------
parser = argparse.ArgumentParser(
    description="AI-powered Network Scanner",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    epilog="Example: ./nmap.py 192.168.1.1 -p 22,80 --profile full"
)


parser.add_argument("target", help="Host / CIDR to scan")
parser.add_argument("-p", "--ports", default="1-1024",
                    help="Port or range (default 1-1024)")
parser.add_argument("--profile", choices=["fast", "full", "vuln"],
                    default="fast", help="Scan profile")
parser.add_argument("--model", default="gpt-4o-mini",
                    help="OpenAI or local model name")
parser.add_argument("--out", default="scan_report.md",
                    help="Write full report to file (md / json)")
args = parser.parse_args()


# ---------- Nmap ----------
flags = {"fast": "-T4 -sS",
        "full": "-T4 -sS -sV -O",
         "vuln": "-T4 -sS -sV --script vuln"}


nm = nmap.PortScanner()
print(f"[+] Scanning {args.target} {args.ports} …")
nm.scan(args.target, args.ports, flags[args.profile])


# ---------- Build prompt ----------
def scan_to_text(nm_obj):
    lines = []
    for host in nm_obj.all_hosts():
        lines.append(f"Host {host} is {nm_obj[host].state()}")
        for proto in nm_obj[host].all_protocols():
            for port in sorted(nm_obj[host][proto]):
                svc = nm_obj[host][proto][port]
                lines.append(f"Port {port}/{proto} {svc['state']} "
                             f"{svc.get('name','')} {svc.get('version','')}")
    return "\n".join(lines)


scan_summary = scan_to_text(nm)

system_msg = textwrap.dedent("""
    You are a senior penetration tester. 
    Explain the risk of each finding, map to any known CVEs,
    prioritise by severity (High/Med/Low), and propose concrete fixes.
""").strip()

messages = [
    {"role": "system", "content": system_msg},
    {"role": "user",   "content": scan_summary}
]



# ---------- LLM ----------
client = OpenAI()                                # API key via env var
chat = client.chat.completions.create(
    model=args.model,
    messages=messages,
    temperature=0.3
)
advice = chat.choices[0].message.content.strip()


# ---------- Output ----------
print("\n[+] Scan complete!\n")

with open(args.out, "w") as f:
    if args.out.endswith(".json"):
        json.dump({
            "target": args.target,
            "ports": args.ports,
            "profile": args.profile,
            "scan_summary": scan_summary,
            "advice": advice
        }, f, indent=2)
    elif args.out.endswith(".md"):
        report = f"""# AI-Powered Scan Report
        ## Scan parameters
        * Target: `{args.target}`
        * Ports : `{args.ports}`
        * Profile: `{args.profile}`

        ## Raw Nmap summary
        ```
        {scan_summary}
        ```

        ## AI Analysis
        ```
        {advice}
        ```
        """

        f.write(report)
    elif args.out.endswith == ".txt":
        f.write(f"Target: {args.target}\n")
        f.write(f"Ports: {args.ports}\n")
        f.write(f"Profile: {args.profile}\n")
        f.write(f"Scan Summary:\n{scan_summary}\n")
        f.write(f"AI Advice:\n{advice}\n")

    else:
        # Display only the scan summary on CLI, not the AI analysis
        print(f"Target: {args.target}")
        print(f"Ports: {args.ports}")
        print(f"Profile: {args.profile}")
        print("Scan Summary:")
        print(scan_summary)

print(f"[+] Full report written to {args.out}\n")