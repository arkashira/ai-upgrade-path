import pytest
from learning_path import LearningPathEngine, Module, LearningPath

def test_generate_learning_path():
    engine = LearningPathEngine()
    role = "ML Engineer"
    goals = ["Learn ML", "Learn DL", "Learn NLP"]
    learning_path = engine.generate_learning_path(role, goals)
    assert len(learning_path.modules) == 4
    assert len(learning_path.modules[0]) == 2
    assert learning_path.modules[0][0].name == "Introduction to ML"
    assert learning_path.modules[0][1].name == "Deep Learning"

def test_update_learning_path():
    engine = LearningPathEngine()
    role = "ML Engineer"
    goals = ["Learn ML", "Learn DL", "Learn NLP"]
    learning_path = engine.generate_learning_path(role, goals)
    new_breakthrough = Module("New Breakthrough", "Learn about new breakthrough")
    engine.update_learning_path(learning_path, new_breakthrough)
    assert len(learning_path.modules) == 5
    assert learning_path.modules[-1][0].name == "New Breakthrough"

def test_reorder_modules():
    engine = LearningPathEngine()
    role = "ML Engineer"
    goals = ["Learn ML", "Learn DL", "Learn NLP"]
    learning_path = engine.generate_learning_path(role, goals)
    engine.reorder_modules(learning_path, 0, 0, 1)
    assert learning_path.modules[0][0].name == "Deep Learning"
    assert learning_path.modules[0][1].name == "Introduction to ML"

def test_skip_module():
    engine = LearningPathEngine()
    role = "ML Engineer"
    goals = ["Learn ML", "Learn DL", "Learn NLP"]
    learning_path = engine.generate_learning_path(role, goals)
    engine.skip_module(learning_path, 0, 0)
    assert len(learning_path.modules[0]) == 1
    assert learning_path.modules[0][0].name == "Deep Learning"
