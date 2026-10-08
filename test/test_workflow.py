from agent.workflow import run_agent

result = run_agent(
    "Add username validation and write tests"
)

print("\nSelected Files")
print(result["selected_files"])

print("\nPlan")
print(result["plan"])

print("\nDiffs")

for file_name, diff in result["diffs"].items():
    print("\n" + "=" * 50)
    print(file_name)
    print("=" * 50)
    print(diff)