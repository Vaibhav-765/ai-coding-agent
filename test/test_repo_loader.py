from services.repo_loader import load_repository

files = load_repository("sample_repo")

for file_name in files:
    print(file_name)