from pathlib import Path
import os

# Define path variables
ROOT_DIR = Path(Path(__file__).resolve().parent.parent)
MODELS_DIR = os.path.join(ROOT_DIR, "models")
DATA_DIR = os.path.join(ROOT_DIR, "data")

