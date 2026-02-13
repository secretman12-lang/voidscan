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

---

## Installation

```bash
git clone https://github.com/secretman12-lang/voidscan.git
cd voidscan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Usage Modes

### 🔹 Normal Mode

Basic username scan.

```bash
python -m voidscan.cli USERNAME
```

![Normal Mode](screenshots/demo.png)

---

### 🔐 Strict Mode

More conservative scan using error signature validation.

```bash
python -m voidscan.cli USERNAME --strict
```

![Strict Mode](screenshots/demo2.png)

---

### 🔥 Deep Mode

Aggressive scan with username variations.

```bash
python -m voidscan.cli USERNAME --deep
```

![Deep Mode](screenshots/demo3.png)

---

### ❓ Help

Display available options.

```bash
python -m voidscan.cli --help
```

![Help](screenshots/demo4.png)

---

## Disclaimer

For educational and legal OSINT research only.  
The author is not responsible for misuse.
