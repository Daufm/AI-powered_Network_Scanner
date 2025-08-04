

# 🔍 AI-Powered Network Scanner

This repository contains Python scripts for intelligent, AI-enhanced network scanning and device discovery. It allows you to scan IP ranges, discover open ports and services, and receive AI-generated security insights and remediation suggestions.

---

## ✨ Features

* 🔎 Fast and customizable Nmap-based scanning
* 🤖 AI-powered risk analysis and fix suggestions (via OpenAI)
* 🖥️ Device and service discovery
* ⚙️ CLI-friendly with configurable scan profiles
* 📝 Output in terminal and optional Markdown/JSON reports

---

## 📦 Requirements

* Python 3.8+
* Nmap (must be installed on your system)
* Python packages listed in `requirements.txt`

---

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Daufm/AI-powered_Network_Scanner.git
   cd AI-powered_Network_Scanner
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Nmap is installed:**

   ```bash
   # Ubuntu/Debian
   sudo apt install nmap

   # macOS
   brew install nmap

   # Windows: https://nmap.org/download.html
   ```

---

## ⚙️ Usage

### 🔧 Basic Scan

```bash
python scanner.py 192.168.1.0/24 --out report.md
```

### 🛡️ With Custom Profile

```bash
python scanner.py 192.168.1.7 -p 1-65535 --profile vuln --out full_report.md
```

### 📁 Output

* Markdown report: `report.md`
* Terminal summary with AI recommendations

---

## 📁 Configuration

* Configure default scan profiles in `scanner.py`
* Store your OpenAI API key via environment variable or `.env` file:

  ```env
  OPENAI_API_KEY=sk-...yourkey...
  ```

---

## 🧪 Example

```bash
python scanner.py 10.0.0.1 --profile full --out results.md
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your fork:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.




---


## ⚠️ Tips for Running the Scanner Smoothly

### ✅ Use a Virtual Environment (`venv`)

To avoid dependency conflicts and keep your Python environment clean:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

This ensures you're using the right versions of the required packages (like `python-nmap`, `openai`, etc.).

---

### 🛠️ Use `$(which python3)` for Scanning (Especially with `sudo`)

Some scan types (like SYN scans) require root access. If you run the scanner with `sudo`, your virtual environment may not be respected unless you use:

```bash
sudo $(which python3) scanner.py 192.168.1.7 --out report.md
```

Why this works:

* `$(which python3)` resolves the full path to your Python binary (including the virtual environment one).
* It prevents errors like:

  * `ModuleNotFoundError: No module named 'nmap'`
  * Nmap scan failures due to missing privileges

---

