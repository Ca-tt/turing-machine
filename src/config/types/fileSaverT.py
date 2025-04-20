from dataclasses import dataclass, field

@dataclass
class SavedData():
    alphabet: str = ""
    rules: dict = field(default_factory=dict)
    task_conditions: str = ""
    comments: str = ""
