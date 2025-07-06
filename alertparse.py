import time
import re
import argparse

# Alert signature patterns
alert_patterns = {
    "Failed Login": r"(failed login|authentication failure|invalid password)",
    "SQL Injection": r"('|--|select|union|or\s1=1)",
    "XSS": r"(<script>|%3Cscript%3E)",
    "File Access": r"(etc/passwd|system32|boot.ini)",
    "Privilege Escalation": r"(sudo|root access|admin rights)"
}

def monitor_log(filepath, output_file=None):
    print(f"\n📡 Monitoring log file: {filepath} (Ctrl+C to stop)\n")

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        f.seek(0, 2)  # Jump to end of file

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            for tag, pattern in alert_patterns.items():
                if re.search(pattern, line, re.IGNORECASE):
                    alert = f"[ALERT] {tag} → {line.strip()}"
                    print(alert)
                    if output_file:
                        with open(output_file, "a") as out:
                            out.write(alert + "\n")
                    break

def main():
    parser = argparse.ArgumentParser(description="🚨 AlertParse - Real-Time Log Parser & Alert System")
    parser.add_argument("-f", "--file", required=True, help="Path to log file")
    parser.add_argument("-o", "--output", help="File to save alert report")
    args = parser.parse_args()

    try:
        monitor_log(args.file, args.output)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped.")

if __name__ == "__main__":
    main()
