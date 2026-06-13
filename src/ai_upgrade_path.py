import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Module:
    name: str
    estimated_time: int
    completed: bool

@dataclass
class Roadmap:
    modules: list[Module]

class AIUpgradePath:
    def __init__(self, roadmap: Roadmap):
        self.roadmap = roadmap
        self.learning_streak = 0
        self.upcoming_modules = []
        self.completion_percentage = 0

    def update_learning_streak(self, completed_modules: list[Module]):
        self.learning_streak = sum(1 for module in completed_modules if module.completed)
        return self.learning_streak

    def get_upcoming_modules(self):
        self.upcoming_modules = [module for module in self.roadmap.modules if not module.completed]
        return self.upcoming_modules

    def calculate_completion_percentage(self):
        completed_modules = sum(1 for module in self.roadmap.modules if module.completed)
        self.completion_percentage = (completed_modules / len(self.roadmap.modules)) * 100
        return self.completion_percentage

    def dashboard(self):
        return {
            'current_streak': self.learning_streak,
            'upcoming_modules': self.upcoming_modules,
            'completion_percentage': self.completion_percentage
        }
