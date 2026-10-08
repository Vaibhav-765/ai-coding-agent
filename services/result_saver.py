from pathlib import Path
import json


OUTPUT_DIR = Path("outputs/generated_patches")


def save_results(result):

    if OUTPUT_DIR.exists() and OUTPUT_DIR.is_file():
        OUTPUT_DIR.unlink()

    print("OUTPUT_DIR =", OUTPUT_DIR)
    print("Exists =", OUTPUT_DIR.exists())
    print("Is Dir =", OUTPUT_DIR.is_dir())
    print("Is File =", OUTPUT_DIR.is_file())

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Selected files
    with open(
        OUTPUT_DIR / "selected_files.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            result["selected_files"],
            f,
            indent=4
        )

    # Plan
    with open(
        OUTPUT_DIR / "plan.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result["plan"])

    # Diffs
    with open(
        OUTPUT_DIR / "diffs.txt",
        "w",
        encoding="utf-8"
    ) as f:

        for file_name, diff in result["diffs"].items():

            f.write(f"\n{'=' * 50}\n")
            f.write(file_name)
            f.write(f"\n{'=' * 50}\n")

            f.write(diff)
            f.write("\n")

    # Modified files
    modified_dir = OUTPUT_DIR / "modified_files"
    modified_dir.mkdir(exist_ok=True)

    for file_name, code in result["modified_files"].items():

        safe_name = file_name.replace("/", "_").replace("\\", "_")

        with open(
            modified_dir / safe_name,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(code)