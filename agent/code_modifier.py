from services.llm import get_llm
from guardrails.code_validator import validate_python_code

llm = get_llm()

def modify_code(task, selected_files, files_data):
    modified_files = {}

    for file_path in selected_files:

        if file_path not in files_data:
            continue

        original_code = files_data[file_path]

        prompt = f"""
        You are a senior Python engineer.
        
        Task:
        {task}

        File Path:
        {file_path}

        Current Code:
        {original_code}

        Instructions:
        1. Modify the code to satisfy the task.
        2. Return the FULL updated file.
        3. Do not explain anything.
        4. Do not use markdown.
        5. Do not wrap the response in triple backticks.
        6. Return only valid Python code.
        """

        print(f"Processing: {file_path}")

        response = llm.invoke(prompt)

        generated_code = response.content
        
        if validate_python_code(generated_code):
            modified_files[file_path] = generated_code

    return modified_files
