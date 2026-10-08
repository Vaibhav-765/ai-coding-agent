from agent.planner import generate_plan

plan = generate_plan(
    "Add input validation and write tests",
    [
        "sample_repo/api.py",
        "sample_repo/validators.py",
        "sample_repo/tests/test_api.py"
    ]
)

print(plan)