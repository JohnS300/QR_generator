import logging
from pathlib import Path


def get_logger(folder, filename: str = "qr_log.txt") -> logging.Logger:
    """
    Configure and return a logger that appends to `folder/filename`.
    """
    log_path = Path(folder) / filename
    logger = logging.getLogger("qr_generator")
    if not logger.handlers:
        handler = logging.FileHandler(log_path, mode='a', encoding='utf-8')
        fmt = logging.Formatter("%(asctime)s — %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(fmt)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger