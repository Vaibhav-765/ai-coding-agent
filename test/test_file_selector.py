from services.repo_loader import load_repository
from agent.file_selector import select_relevant_files

files = load_repository("sample_repo")

task = "Add input validation and write tests"

result = select_relevant_files(task, files)

print(result)