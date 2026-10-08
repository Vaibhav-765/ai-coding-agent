from services.llm import get_llm

llm = get_llm()

def generate_plan(task, selected_files):
    prompt = f"""
Task:
{task}

Relevant Files:
{selected_files}

Create a short implementation plan.

Return 3-5 steps.
"""

    response = llm.invoke(prompt)

    return response.content