import pytest
from learning_path import LearningPathEngine, Module, LearningPath

def test_generate_learning_path():
    engine = LearningPathEngine()
    learning_path = engine.generate_learning_path("ML Engineer", ["goal1", "goal2", "goal3"])
    assert learning_path.role == "ML Engineer"
    assert learning_path.goals == ["goal1", "goal2", "goal3"]
    assert len(learning_path.modules) == 8

def test_update_learning_path():
    engine = LearningPathEngine()
    learning_path = engine.generate_learning_path("ML Engineer", ["goal1", "goal2", "goal3"])
    updated_learning_path = engine.update_learning_path(learning_path)
    assert updated_learning_path == learning_path

def test_reorder_modules():
    engine = LearningPathEngine()
    learning_path = engine.generate_learning_path("ML Engineer", ["goal1", "goal2", "goal3"])
    new_module_order = [1, 0, 2, 3, 4, 5, 6, 7]
    reordered_learning_path = engine.reorder_modules(learning_path, new_module_order)
    assert reordered_learning_path.modules[0].name == learning_path.modules[1].name

def test_skip_module():
    engine = LearningPathEngine()
    learning_path = engine.generate_learning_path("ML Engineer", ["goal1", "goal2", "goal3"])
    skipped_learning_path = engine.skip_module(learning_path, 0)
    assert len(skipped_learning_path.modules) == 7
