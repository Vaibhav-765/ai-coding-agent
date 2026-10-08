from typing import Dict, List, TypedDict

class AgentState(TypedDict):
    task: str
    files_data: Dict[str, str]
    selected_files: List[str]
    plan: str
    modified_code: Dict[str, str]
    diff: str