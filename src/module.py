import json
from dataclasses import dataclass
from typing import List

@dataclass
class Module:
    title: str
    length: int
    exercises: List[str]
    content: str

    def render(self, mode: str) -> str:
        if mode == "dark":
            return f"<div style='background-color: #333; color: #fff'>{self.content}</div>"
        else:
            return f"<div>{self.content}</div>"

    def update_progress(self, step: int) -> int:
        if step < 1 or step > 2:
            raise ValueError("Invalid exercise step")
        return step

def create_module(title: str, length: int, exercises: List[str], content: str) -> Module:
    if length < 5 or length > 10:
        raise ValueError("Module length must be between 5-10 minutes")
    return Module(title, length, exercises, content)
