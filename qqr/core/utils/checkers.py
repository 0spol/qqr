import re
from typing import List
from qqr.core.utils.options import ErrorTolerance, Format

def text_path_check(text: str) -> bool:
    if not text or not isinstance(text, str):
        return False
    if len(text) > 2000:
        return False
    if not all(32 <= ord(c) <= 126 for c in text):
        return False
    return True

def error_check(error: str) -> bool:
    if error not in ErrorTolerance:
        return False
    return True

def format_check(formats: List[str]) -> bool:
    if not formats:
        return False
    for fmt in formats:
        if fmt not in Format:
            return False
    return True

def name_check(name: str) -> bool:
    if not name or not isinstance(name, str):
        return False
    if len(name) > 255:
        return False
    if not re.match(r'^[a-zA-Z0-9_-]+$', name):
        return False
    return True

def color_check(color: str) -> bool:
    if not color or not isinstance(color, str):
        return False
    if re.match(r"^#([A-Fa-f0-9]{6})$", color):
        return True
    valid_names = {
        "black", "white", "red", "green", "blue",
        "yellow", "cyan", "magenta", "gray", "grey"
    }
    if color.lower() in valid_names:
        return True
    return True