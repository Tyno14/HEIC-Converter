# HEIC Converter

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![HEIC Converter](https://img.shields.io/badge/Convertisseur-HEIC→JPG%2FPNG%2FWEBP-brightgreen)
![Licence MIT](https://img.shields.io/badge/Licence-MIT-yellow)

---

> 🇫🇷 *version française ci-dessous ↓*

---

**Application graphique Python pour convertir facilement des images `.heic` (format Apple) vers `.jpg`, `.png` ou `.webp`.**   Le tout **localement**, sans envoyer ses photos sur internet.

---

## 🔧 Fonctionnalités

- Convertir un dossier ou plusieurs fichiers `.heic`
- Glisser-déposer directement dans l'interface
- Choix du format de sortie (JPG, PNG, WEBP)
- Suppression automatique des fichiers `.heic` après conversion (optionnel)

---

## Dépendances

Le projet utilise les bibliothèques suivantes :

- [`Pillow`](https://pypi.org/project/Pillow/)
- [`pillow-heif`](https://pypi.org/project/pillow-heif/)
- [`tkinterdnd2`](https://pypi.org/project/tkinterdnd2/)

---

## Installation

### 📦 Téléchargement

- [Télécharger le `.exe` pour Windows](https://github.com/Tyno14/HEIC-Converter/releases/download/v1.0/HEIC-converter.exe)
- [Télécharger le `.deb` pour Debian/Ubuntu](https://github.com/Tyno14/HEIC-Converter/releases/download/v1.0/HEIC-converter-1.0.deb)

> Aucun envoi de données : tout est exécuté **localement** sur votre machine.

---

### 🛠️ Installation manuelle (Linux / macOS / Windows)

```bash
git clone https://github.com/Tyno14/HEIC-Converter.git
cd HEIC-Converter
python3 -m venv .venv
source .venv/bin/activate  # sous Windows : .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### 🛡️ Licence

Ce projet est sous licence MIT – voir le fichier [LICENSE](LICENSE) pour plus d’informations.

---
> *🇬🇧 English version above ↓*

## EN - HEIC Converter

**A simple Python GUI application to convert `.heic` images (Apple format) into `.jpg`, `.png`, or `.webp`.** Everything runs **locally**, so your photos stay on your machine — nothing is uploaded online.

### 🔧 Features

- Convert an entire folder or multiple `.heic` files
- Drag and drop into the interface
- Choose the output format (JPG, PNG, or WEBP)
- Optional deletion of original `.heic` files

### 🧪 Dependencies

- [`Pillow`](https://pypi.org/project/Pillow/)
- [`pillow-heif`](https://pypi.org/project/pillow-heif/)
- [`tkinterdnd2`](https://pypi.org/project/tkinterdnd2/)

### Install

#### 📦 Quick download

- [Download `.exe` for Windows](https://github.com/Tyno14/HEIC-Converter/releases/download/v1.0/HEIC-converter.exe)
- [Download `.deb` for Debian/Ubuntu](https://github.com/Tyno14/HEIC-Converter/releases/download/v1.0/HEIC-converter-1.0.deb)

> No data is ever sent — all processing is done **locally**.

#### 🛠️ Manual install (Linux / macOS / Windows)

```bash
git clone https://github.com/Tyno14/HEIC-Converter.git
cd HEIC-Converter
python3 -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### 🛡️ License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
