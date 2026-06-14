from ai_upgrade_path import Module, Roadmap, calculate_streak, get_upcoming_modules, calculate_completion_percentage, get_dashboard
from datetime import datetime, timedelta
import pytest

def test_calculate_streak():
    module1 = Module("Module 1", 10, True, datetime.now() - timedelta(days=1))
    module2 = Module("Module 2", 20, False)
    roadmap = Roadmap([module1, module2])
    assert calculate_streak(roadmap) == 1

def test_calculate_streak_no_completed_modules():
    module1 = Module("Module 1", 10, False)
    module2 = Module("Module 2", 20, False)
    roadmap = Roadmap([module1, module2])
    assert calculate_streak(roadmap) == 0

def test_get_upcoming_modules():
    module1 = Module("Module 1", 10, True, datetime.now() - timedelta(days=1))
    module2 = Module("Module 2", 20, False)
    roadmap = Roadmap([module1, module2])
    upcoming_modules = get_upcoming_modules(roadmap)
    assert len(upcoming_modules) == 1
    assert upcoming_modules[0].name == "Module 2"

def test_calculate_completion_percentage():
    module1 = Module("Module 1", 10, True, datetime.now() - timedelta(days=1))
    module2 = Module("Module 2", 20, False)
    roadmap = Roadmap([module1, module2])
    assert calculate_completion_percentage(roadmap) == 50.0

def test_get_dashboard():
    module1 = Module("Module 1", 10, True, datetime.now() - timedelta(days=1))
    module2 = Module("Module 2", 20, False)
    roadmap = Roadmap([module1, module2])
    dashboard = get_dashboard(roadmap)
    assert "streak" in dashboard
    assert "upcoming_modules" in dashboard
    assert "completion_percentage" in dashboard
