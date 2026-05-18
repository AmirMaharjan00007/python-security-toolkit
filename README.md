# 🛡️ Lightweight Python scripts that act as your first line of defense.

A modular, open-source collection of Python security tools for analyzing logs, auditing credentials, detecting threats, and generating reports — all from your terminal. No bloated frameworks, just clean scripts you can read, modify, and trust.

---

## 🔧 Tools Included

| Script | Description |
|---|---|
| `log_analyzer.py` | Parses auth logs and flags IPs with repeated failed login attempts |
| `password_checker.py` | Evaluates password strength against common rules and patterns |
| `file_integrity.py` | Hashes files and detects unauthorized changes over time |
| `ip_reputation.py` | Looks up IPs against threat intelligence sources |
| `phishing_detector.py` | Analyzes URLs for phishing indicators and suspicious patterns |
| `port_scanner.py` | Scans a host for open ports and identifies running services |
| `report_generator.py` | Aggregates findings from other tools into a unified security report |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sentinel-py.git
cd sentinel-py

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📖 Usage

### Log Analyzer
```bash
python log_analyzer.py
# Edit LOG_FILE_PATH inside the script to point to your auth log
# Default: /var/log/auth.log (requires sudo on Linux)
```

### Password Strength Checker
```bash
python password_checker.py
# Enter passwords interactively; get scored feedback
```

### File Integrity Checker
```bash
python file_integrity.py --init /path/to/directory     # Create baseline hashes
python file_integrity.py --check /path/to/directory    # Detect changes
```

### IP Reputation Tracker
```bash
python ip_reputation.py --ip 192.168.1.10
python ip_reputation.py --file ips.txt                 # Batch lookup
```

### Phishing URL Detector
```bash
python phishing_detector.py --url "http://example.com"
python phishing_detector.py --file urls.txt
```

### Port Scanner
```bash
python port_scanner.py --host 192.168.1.1
python port_scanner.py --host 192.168.1.1 --ports 1-1024
```

### Security Report Generator
```bash
python report_generator.py --output report.txt
# Reads output files from other tools and compiles a unified report
```

---

## 📁 Project Structure

```
sentinel-py/
├── log_analyzer.py
├── password_checker.py
├── file_integrity.py
├── ip_reputation.py
├── phishing_detector.py
├── port_scanner.py
├── report_generator.py
├── requirements.txt
├── samples/
│   ├── sample_auth.log
│   └── sample_urls.txt
├── reports/              # Generated reports saved here (gitignored)
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Configuration

Each script has a configuration block at the top of the file. Edit the constants directly:

```python
# Example from log_analyzer.py
LOG_FILE_PATH = "/var/log/auth.log"   # Path to your log file
FAILED_THRESHOLD = 5                  # Flag IPs with more than this many attempts
OUTPUT_REPORT = "reports/security_report.txt"
```

---

## 🤝 Contributing

Contributions are welcome! To add a new tool or improve an existing one:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-tool-name`
3. Write clean, documented Python with a config block at the top
4. Add usage instructions to this README
5. Submit a pull request

Please keep scripts self-contained and dependency-light where possible.

---

## ⚠️ Disclaimer

These tools are intended for **educational purposes and authorized security testing only**. Do not use them against systems you do not own or have explicit permission to test. The author is not responsible for misuse.

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## ⭐ Star this repo if you find it useful!

---

Last Updated, May 2026
Amir Maharjan

---
