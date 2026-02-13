# VoidScan

Scanner OSINT Experimental de Usernames

---

## 📌 Sobre

O VoidScan é uma ferramenta OSINT experimental para busca de usernames em múltiplas plataformas.

Possui modo estrito e modo agressivo para diferentes níveis de análise.

---

## 🚀 Funcionalidades

- Varredura assíncrona (async)
- Modo Normal
- Modo Strict (mais preciso)
- Modo Deep (agressivo com variações)
- Geração automática de variações de username
- Interface CLI com Rich
- Arquitetura modular

---

## 💻 Instalação

```bash
git clone https://github.com/secretman12-lang/voidscan.git
cd voidscan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🛠 Modos de Uso

### 🔹 Modo Normal

Verifica apenas o username original.

```bash
python -m voidscan.cli USERNAME
```

![Modo Normal](screenshots/demo.png)

---

### 🔐 Modo Strict

Modo mais conservador, valida assinatura de erro do site.

```bash
python -m voidscan.cli USERNAME --strict
```

![Modo Strict](screenshots/demo2.png)

---

### 🔥 Modo Deep

Modo agressivo, gera variações do username.

```bash
python -m voidscan.cli USERNAME --deep
```

![Modo Deep](screenshots/demo3.png)

---

### ❓ Ajuda

```bash
python -m voidscan.cli --help
```

![Ajuda](screenshots/demo4.png)

---

## ⚠ Aviso

Esta ferramenta é destinada apenas para fins educacionais e pesquisa OSINT legal.

O autor não se responsabiliza por uso indevido.
