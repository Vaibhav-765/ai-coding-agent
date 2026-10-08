from services.repo_loader import load_repository
from agent.file_selector import select_relevant_files
from agent.planner import generate_plan
from agent.code_modifier import modify_code
from agent.diff_generator import generate_diff
from agent.explainer import generate_explanation
from guardrails.task_validator import validate_task


def run_agent(task, repo_path="sample_repo"):

    explanation = ""
    plan = ""
    modified_files = {}
    diffs = {}
    
    validate_task(task)

    files_data = load_repository(repo_path)

    selected_files = select_relevant_files(
        task,
        files_data
    )

    plan = generate_plan(
        task,
        selected_files
    )

    modified_files = modify_code(
        task,
        selected_files,
        files_data
    )

    diffs = {}

    for file_path, modified_code in modified_files.items():

        original_code = files_data[file_path]

        diffs[file_path] = generate_diff(
            original_code,
            modified_code,
            file_path
        )
        
        if diffs:
            explanation = generate_explanation(
                task,
                diffs
            )
        else:
            explanation = "No code changes were generated."

    return {
        "task": task,
        "selected_files": selected_files,
        "plan": plan,
        "modified_files": modified_files,
        "diffs": diffs,
        "explanation": explanation
}