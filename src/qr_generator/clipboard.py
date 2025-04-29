import pyperclip


def copy_to_clipboard(path: str) -> None:
    """
    Copy the given file path string to the system clipboard.
    """
    pyperclip.copy(str(path))