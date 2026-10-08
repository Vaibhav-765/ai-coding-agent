from services.llm import get_llm

llm = get_llm()


def judge_result(task, diff):

    prompt = f"""
Task:
{task}

Generated Diff:
{diff}

Score from 1-10.

Return JSON:

{{
 "score": 8,
 "reason": "..."
}}
"""

    response = llm.invoke(prompt)

    return response.content