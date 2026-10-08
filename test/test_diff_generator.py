from services.repo_loader import load_repository
from agent.code_modifier import modify_code
from agent.diff_generator import generate_diff

files_data = load_repository("sample_repo")

selected_files = [
    "sample_repo/user_service.py"
]

modified_files = modify_code(
    "Add username validation",
    selected_files,
    files_data
)

for file_path, modified_code in modified_files.items():

    original_code = files_data[file_path]

    diff = generate_diff(
        original_code,
        modified_code,
        file_path
    )

    print(diff)