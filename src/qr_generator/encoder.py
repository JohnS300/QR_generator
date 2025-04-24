import hashlib


def short_hash(data: str, length: int = 6) -> str:
    """
    Generate an MD5 digest of `data` and return the first `length` characters.
    """
    digest = hashlib.md5(data.encode('utf-8')).hexdigest()
    return digest[:length]