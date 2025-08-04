

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
