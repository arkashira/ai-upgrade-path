from ai_upgrade_path import AIUpgradePath, Module, Roadmap
import pytest

def test_learning_streak():
    roadmap = Roadmap([Module('module1', 1, True), Module('module2', 2, False)])
    ai_upgrade_path = AIUpgradePath(roadmap)
    ai_upgrade_path.update_learning_streak(roadmap.modules)
    assert ai_upgrade_path.learning_streak == 1

def test_upcoming_modules():
    roadmap = Roadmap([Module('module1', 1, True), Module('module2', 2, False)])
    ai_upgrade_path = AIUpgradePath(roadmap)
    upcoming_modules = ai_upgrade_path.get_upcoming_modules()
    assert len(upcoming_modules) == 1
    assert upcoming_modules[0].name == 'module2'

def test_completion_percentage():
    roadmap = Roadmap([Module('module1', 1, True), Module('module2', 2, False)])
    ai_upgrade_path = AIUpgradePath(roadmap)
    completion_percentage = ai_upgrade_path.calculate_completion_percentage()
    assert completion_percentage == 50.0

def test_dashboard():
    roadmap = Roadmap([Module('module1', 1, True), Module('module2', 2, False)])
    ai_upgrade_path = AIUpgradePath(roadmap)
    ai_upgrade_path.update_learning_streak(roadmap.modules)
    ai_upgrade_path.get_upcoming_modules()
    ai_upgrade_path.calculate_completion_percentage()
    dashboard = ai_upgrade_path.dashboard()
    assert 'current_streak' in dashboard
    assert 'upcoming_modules' in dashboard
    assert 'completion_percentage' in dashboard
