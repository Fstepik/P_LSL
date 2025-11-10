# LSL - Lokální spouštěcí lišta
Nadupaný program umožnující přehlednou formou nabídnout exe soubory z množiny složek. Např. ze složky GINIS. Nabízejí se soubory začínající na GSA a končící 01, podmínkou je _x64 architektura daného prográmku, jinak se nenabídne.


# Struktura Python projektu – Popis souborů a složek

Tento dokument popisuje nejběžněji používané soubory a složky v typickém Python projektu, včetně složek používaných při kompilaci pomocí PyInstaller.

| Název                  | Typ      | Popis                                                                 |
|------------------------|----------|-----------------------------------------------------------------------|
| `main.py` / `spoustec.py` | soubor   | Hlavní skript aplikace – zde je logika programu.                      |
| `README.md`           | soubor   | Popis projektu, návod k použití, poznámky k verzím.                   |
| `.gitignore`          | soubor   | Určuje, které soubory/složky Git ignoruje (např. `dist/`, `*.exe`).   |
| `requirements.txt`    | soubor   | Seznam knihoven potřebných k běhu projektu (např. `Pillow`, `pywin32`).|
| `assets/`             | složka   | Statické soubory používané aplikací – obrázky, ikony, zvuky, fonty.   |
| `releases/`           | složka   | Archiv hotových verzí aplikace – např. `lsl_v1.0.exe`.                |
| `dist/`               | složka   | Výstup z kompilace pomocí PyInstaller – obsahuje `.exe` soubor.       |
| `build/`              | složka   | Dočasné soubory vytvořené při kompilaci – technické mezivýsledky.     |
| `__pycache__/`        | složka   | Automaticky generovaná složka s cache Pythonu – není potřeba verzovat.|
| `*.spec`              | soubor   | Konfigurační soubor vytvořený PyInstallerem – popisuje jak se má projekt kompilovat. |
| `.vscode/` / `.idea/` | složka   | Nastavení vývojového prostředí (VS Code, PyCharm) – není nutné verzovat.|

---

## 🧠 Doporučení

- Verzuj jen to, co je důležité pro vývoj a běh aplikace.
- Ignoruj složky jako `dist/`, `build/`, `__pycache__/` pomocí `.gitignore`.
- Udržuj `README.md` a `releases/` pro přehled o verzích.
