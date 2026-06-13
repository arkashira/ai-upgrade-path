import pytest
from src.roadmap import RoadmapGenerator
from src.models import User

def test_generate():
    generator = RoadmapGenerator()
    user = User('test@example.com', 'developer', ['learn python', 'learn java'])
    roadmap = generator.generate(user)
    assert roadmap.weeks == 1
    assert roadmap.goals == ['learn python', 'learn java']
