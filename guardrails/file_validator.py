from pathlib import Path

ALLOWED_EXTENSIONS = [
    ".py",
    ".js",
    ".ts"
]


def is_allowed_file(file_path):

    ext = Path(file_path).suffix

    return ext in ALLOWED_EXTENSIONS