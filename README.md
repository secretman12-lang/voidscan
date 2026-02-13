# VoidScan

🇧🇷 Leia em Português: [README.pt-BR](README.pt-BR.md)

Advanced Experimental OSINT Username Scanner

---

## Features

- Async scanning
- Strict and Deep modes
- Username variations
- CLI interface
- Modular architecture
- Installable via pip

---

## 🖥 Supported Operating Systems

- Linux
- Windows
- macOS
- Termux (Android)
- Any system with Python 3.10+

---

## Installation & Usage

```bash
# Install via pip
pip install voidscan

# or install from source
git clone https://github.com/secretman12-lang/voidscan.git
cd voidscan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# -------------------------
# 🚀 Usage Modes
# -------------------------

# 🔹 Normal Mode
voidscan USERNAME
# or
python -m voidscan.cli USERNAME

# 🔐 Strict Mode
voidscan USERNAME --strict
# or
python -m voidscan.cli USERNAME --strict

# 🔥 Deep Mode
voidscan USERNAME --deep
# or
python -m voidscan.cli USERNAME --deep

# ❓ Help
voidscan --help
# or
python -m voidscan.cli --help
```

![Normal Mode](screenshots/demo.png)
![Strict Mode](screenshots/demo2.png)
![Deep Mode](screenshots/demo3.png)
![Help](screenshots/demo4.png)

---

## Disclaimer

For educational and legal OSINT research only.  
The author is not responsible for misuse.
