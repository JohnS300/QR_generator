import os
from pathlib import Path


def ensure_dir(path):
    """
    Create directory (and parents) if it does not exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)