# HEIC Converter

Application graphique Python pour convertir des images `.heic` (Apple) en `.jpg`, `.png` ou `.webp` en local pour ne pas mettre ses photos n'importe ou sur internet ;)

## 🔧 Fonctionnalités

- 📂 Convertir un dossier ou plusieurs fichiers `.heic`
- 🖱️ Glisser-déposer directement dans l'interface
- ✅ Choix du format de sortie (jpg, png, webp)
- 🗑️ Suppression automatique des fichiers `.heic` (optionnel)

## 🧪 Dépendances

- `Pillow`
- `pillow-heif`
- `tkinterdnd2`

## 🚀 Installation

### Linux / Mac / Windows (Python installé)

```bash
git clone https://github.com/.../heicconverter.git
cd heicconverter
python3 -m venv .venv
source .venv/bin/activate  # (ou .venv\\Scripts\\activate sous Windows)
pip install -r requirements.txt
python main.py
```
