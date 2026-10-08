import zipfile
import shutil
from pathlib import Path


def extract_repo(zip_file_path, extract_to="uploaded_repo"):

    extract_path = Path(extract_to)

    if extract_path.exists():
        shutil.rmtree(extract_path)

    extract_path.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    return str(extract_path)