import importlib.util
import subprocess
import sys

# Seznam požadovaných balíčků: {název_modulu: název_pip_balíčku}
packages = {
    "PIL": "Pillow",
    "win32con": "pywin32"
}

def install_package(package_name):
    """Instaluje balíček pomocí pip."""
    print(f"📦 Instaluji {package_name}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def is_installed(module_name):
    """Vrací True, pokud je modul dostupný."""
    spec = importlib.util.find_spec(module_name)
    return spec is not None

if __name__ == "__main__":
    for module, package in packages.items():
        if not is_installed(module):
            install_package(package)
        else:
            print(f"✅ {package} už je nainstalovaný.")

    print("\n✅ Vše hotovo! Můžete bezpečně používat PIL (Pillow) a win32con.")
