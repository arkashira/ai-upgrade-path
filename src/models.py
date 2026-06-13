from dataclasses import dataclass

@dataclass
class User:
    email: str
    role: str
    goals: list

@dataclass
class Roadmap:
    weeks: int
    goals: list
