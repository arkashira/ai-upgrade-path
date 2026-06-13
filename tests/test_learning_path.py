import pytest
from learning_path import LearningPath

def test_generate_path():
    learning_path = LearningPath(role="ML Engineer", goals=["Improve ML skills", "Learn AI ethics", "Explore new tools"])
    learning_path.generate_path()
    
    assert len(learning_path.modules) == 8
    assert learning_path.modules[0].title == "Introduction to AI"
    assert learning_path.modules[1].description == "Fundamentals of machine learning."

def test_to_json():
    learning_path = LearningPath(role="Data Scientist", goals=["Data analysis", "Model deployment", "AI ethics"])
    learning_path.generate_path()
    json_output = learning_path.to_json()
    
    assert '"role": "Data Scientist"' in json_output
    assert '"goals": ["Data analysis", "Model deployment", "AI ethics"]' in json_output
    assert '"modules":' in json_output
