import sys
import argparse
from .config import DEFAULT_FOLDER, DEFAULT_FILL, DEFAULT_BACK, DEFAULT_HASH_LEN
from .encoder import short_hash
from .image import build_qr
from .clipboard import copy_to_clipboard
from .filesystem import ensure_dir
from .logger import get_logger


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a QR code and copy its path to the clipboard"
    )
    parser.add_argument(
        "data", nargs="?", help="Data to encode (if omitted, prompts you)"
    )
    parser.add_argument(
        "-f", "--folder", default=DEFAULT_FOLDER,
        help="Output folder"
    )
    parser.add_argument(
        "--fill", default=DEFAULT_FILL,
        help="QR fill color"
    )
    parser.add_argument(
        "--back", default=DEFAULT_BACK,
        help="QR background color"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # prompt if no data
    if not args.data:
        args.data = input("Enter text/URL to encode: ").strip()
        if not args.data:
            print("No input provided. Exiting.")
            sys.exit(1)

    # ensure output directory exists
    ensure_dir(args.folder)

    # generate image
    img = build_qr(args.data, args.fill, args.back)
    filename = f"qr_code_{short_hash(args.data, DEFAULT_HASH_LEN)}.png"
    filepath = args.folder / filename if hasattr(args.folder, '__truediv__') else f"{args.folder}/{filename}"
    img.save(filepath)

    # copy path and log
    copy_to_clipboard(filepath)
    logger = get_logger(args.folder)
    logger.info(f"{filename}: {args.data}")

    print(f"QR code saved to {filepath} (path copied to clipboard)")