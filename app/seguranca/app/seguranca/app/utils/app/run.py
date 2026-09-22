import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
APP = ROOT / "app"

sys.path.insert(0, str(APP))


from main import Aplicacao


if __name__ == "__main__":
    Aplicacao().executar()
