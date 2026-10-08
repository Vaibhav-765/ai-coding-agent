import difflib

def generate_diff(original_code, modified_code, file_name):
    diff = difflib.unified_diff(
        original_code.splitlines(),
        modified_code.splitlines(),
        fromfile=f"{file_name}_old",
        tofile=f"{file_name}_new",
        lineterm=""
    )

    return "\n".join(diff)
