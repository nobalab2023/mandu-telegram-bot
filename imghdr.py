# imghdr.py – Python 3.13용 간이 shim
from typing import Optional
import filetype

def what(file, h: Optional[bytes] = None):
    try:
        kind = filetype.guess(h if h is not None else file)
        if not kind:
            return None
        mapping = {
            'jpeg': 'jpeg', 'jpg': 'jpeg', 'png': 'png',
            'gif': 'gif', 'bmp': 'bmp', 'tiff': 'tiff', 'webp': 'webp'
        }
        return mapping.get(kind.extension)
    except Exception:
        return None
