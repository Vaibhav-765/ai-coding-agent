import json
from services.llm import get_llm

llm = get_llm()


def select_relevant_files(task, files_data):
    file_list = "\n".join(files_data.keys())

    prompt = f"""
You are a senior software engineer.

Task:
{task}

Available Files:
{file_list}

Return ONLY valid JSON in this format:

{{
  "files": [
    "path/to/file1.py",
    "path/to/file2.py"
  ]
}}

Rules:
- Only choose files from Available Files.
- Do not add explanations.
- Do not use markdown.
"""

    response = llm.invoke(prompt)

    try:
        result = json.loads(response.content)
        selected_files = result.get("files", [])
    except json.JSONDecodeError:
        selected_files = []

    # Safety: keep only files that actually exist
    selected_files = [
        file_path
        for file_path in selected_files
        if file_path in files_data
    ]

    return selected_files