from services.repo_loader import load_repository
from agent.code_modifier import modify_code

print("Test started")

files_data = load_repository("sample_repo")
print("Files loaded:", files_data.keys())

selected_files = [
    "sample_repo/user_service.py"
]

print("Selected files:", selected_files)

result = modify_code(
    "Add username validation",
    selected_files,
    files_data
)

print("Result received")

for file_name, code in result.items():
    print("\n" + "=" * 50)
    print(file_name)
    print("=" * 50)
    print(code)