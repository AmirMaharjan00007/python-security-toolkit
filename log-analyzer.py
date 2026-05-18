import re
from collections import defaultdict
from datetime import datetime

# Configuration
LOG_FILE_PATH = "/var/log/auth.log"     # adjust as needed
OUTPUT_REPORT = "security_report.txt"   # optional output file
FAILED_THRESHOLD = 5                    # IPs with > this many failed attempts are flagged

# Known patterns for failed login lines (Ubuntu/Debian SSH)
FAILED_PATTERNS = [
    r"Failed password for .* from ([\d\.]+)",
    r"Failed password for .* from ([\d\.:a-fA-F]+)",  # also IPv6 friendly
    r"Invalid user .* from ([\d\.]+)",
    r"authentication failure.*rhost=([\d\.]+)",
]

COMPILED_PATTERNS = [re.compile(pat) for pat in FAILED_PATTERNS]

def extract_ip_from_line(line):
    """Try to extract IP from failed login line using multiple patterns."""
    for pat in COMPILED_PATTERNS:
        m = pat.search(line)
        if m:
            return m.group(1)
    return None

def analyze_log(log_path):
    ip_counts = defaultdict(int)

    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f, 1):
                ip = extract_ip_from_line(line)
                if ip:
                    ip_counts[ip] += 1
    except FileNotFoundError:
        print(f"Error: Log file not found: {log_path}")
        return None
    except PermissionError:
        print(f"Error: Permission denied reading {log_path}. Run as root/sudo if needed.")
        return None

    return ip_counts

def generate_report(ip_counts):
    if not ip_counts:
        print("No failed login attempts found.")
        return

    total_failures = sum(ip_counts.values())
    flagged_ips = {ip: count for ip, count in ip_counts.items() if count > FAILED_THRESHOLD}

    print("=" * 60)
    print("      SECURITY REPORT – FAILED LOGIN ATTEMPTS")
    print("=" * 60)
    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total failed attempts: {total_failures}")
    print(f"IPs with > {FAILED_THRESHOLD} failed attempts: {len(flagged_ips)}")
    print()

    print("All IPs (sorted by count descending):")
    print("-" * 50)
    for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
        status = "FLAGGED" if count > FAILED_THRESHOLD else "normal"
        print(f"{ip:16} : {count:4} attempts ({status})")

    # Optional: write to file
    try:
        with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
            f.write("SECURITY REPORT – FAILED LOGIN ATTEMPTS\n")
            f.write("="*50 + "\n")
            f.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total failed attempts: {total_failures}\n")
            f.write(f"IPs with > {FAILED_THRESHOLD} failed attempts: {len(flagged_ips)}\n\n")
            f.write("IP\t\tFailed Attempts\tStatus\n")
            for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
                status = "FLAGGED" if count > FAILED_THRESHOLD else "normal"
                f.write(f"{ip}\t{count}\t{status}\n")
        print(f"\nReport saved to: {OUTPUT_REPORT}")
    except PermissionError:
        print(f"Warning: Could not write to {OUTPUT_REPORT} (permission issue).")

def main():
    print("Log analyzer: failed login attempts per IP")
    print("Analyzing log file:", LOG_FILE_PATH)
    ip_counts = analyze_log(LOG_FILE_PATH)
    if ip_counts is not None:
        generate_report(ip_counts)

if __name__ == "__main__":
    main()
