import json

from evaluation.metrics import evaluate_file_selection
from services.repo_loader import load_repository
from agent.file_selector import select_relevant_files


files_data = load_repository("sample_repo")

with open(
    "evaluation/test_cases.json",
    "r",
    encoding="utf-8"
) as f:

    test_cases = json.load(f)

for test in test_cases:

    task = test["task"]

    expected = test["expected_files"]

    predicted = select_relevant_files(
        task,
        files_data
    )

    metrics = evaluate_file_selection(
        expected,
        predicted
    )

    print("\n" + "=" * 50)
    print("Task:", task)
    print("Expected:", expected)
    print("Predicted:", predicted)
    print("Precision:", metrics["precision"])
    print("Recall:", metrics["recall"])
    print("F1:", metrics["f1"])