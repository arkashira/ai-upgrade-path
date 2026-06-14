from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Module:
    name: str
    estimated_time: int
    completed: bool
    completion_date: datetime = None

@dataclass
class Roadmap:
    modules: List[Module]

def calculate_streak(roadmap: Roadmap) -> int:
    """Calculate the current learning streak in days."""
    completed_modules = [module for module in roadmap.modules if module.completed and module.completion_date]
    if not completed_modules:
        return 0
    latest_completion_date = max(module.completion_date for module in completed_modules)
    today = datetime.now()
    streak = (today - latest_completion_date).days
    return streak

def get_upcoming_modules(roadmap: Roadmap) -> List[Module]:
    """Get the list of upcoming modules."""
    return [module for module in roadmap.modules if not module.completed]

def calculate_completion_percentage(roadmap: Roadmap) -> float:
    """Calculate the completion percentage of the roadmap."""
    total_modules = len(roadmap.modules)
    completed_modules = len([module for module in roadmap.modules if module.completed])
    return (completed_modules / total_modules) * 100

def get_dashboard(roadmap: Roadmap) -> dict:
    """Get the dashboard data."""
    streak = calculate_streak(roadmap)
    upcoming_modules = get_upcoming_modules(roadmap)
    completion_percentage = calculate_completion_percentage(roadmap)
    return {
        "streak": streak,
        "upcoming_modules": upcoming_modules,
        "completion_percentage": completion_percentage
    }
