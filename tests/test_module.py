import pytest
from module import Module, create_module

def test_module_length_metadata():
    module = create_module("Test Module", 7, ["exercise1", "exercise2"], "Test content")
    assert module.length == 7

def test_module_includes_practical_exercise():
    module = create_module("Test Module", 7, ["exercise1", "exercise2"], "Test content")
    assert len(module.exercises) == 2

def test_content_rendered_in_responsive_ui():
    module = create_module("Test Module", 7, ["exercise1", "exercise2"], "Test content")
    assert "<div>" in module.render("light")
    assert "<div style='background-color: #333; color: #fff'>" in module.render("dark")

def test_progress_bar_updates_after_each_exercise_step():
    module = create_module("Test Module", 7, ["exercise1", "exercise2"], "Test content")
    assert module.update_progress(1) == 1
    assert module.update_progress(2) == 2

def test_module_length_out_of_range():
    with pytest.raises(ValueError):
        create_module("Test Module", 3, ["exercise1", "exercise2"], "Test content")

def test_invalid_exercise_step():
    module = create_module("Test Module", 7, ["exercise1", "exercise2"], "Test content")
    with pytest.raises(ValueError):
        module.update_progress(3)
