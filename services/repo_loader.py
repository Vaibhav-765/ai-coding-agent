from pathlib import Path
from guardrails.file_validator import is_allowed_file

def load_repository(repo_path: str):
    files_data = {}

    repo = Path(repo_path)

    for file in repo.rglob("*.py"):
        try:
            files_data[file.as_posix()] = file.read_text(encoding="utf-8")
        except Exception:
            continue

    return files_data