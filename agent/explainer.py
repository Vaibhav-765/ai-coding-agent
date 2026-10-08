from services.llm import get_llm

llm = get_llm()


def generate_explanation(task, diffs):

    diff_text = ""

    for file_name, diff in diffs.items():
        diff_text += f"\nFile: {file_name}\n"
        diff_text += diff
        diff_text += "\n"

    prompt = f"""
You are a senior software engineer.

Task:
{task}

Code Changes:
{diff_text}

Explain:
1. What was changed.
2. Why it was changed.
3. Which files were affected.

Keep the explanation concise and professional.
"""

    response = llm.invoke(prompt)

    return response.content