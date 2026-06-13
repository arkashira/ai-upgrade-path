import pytest
from src.dashboard import Dashboard
from src.models import User

def test_redirect():
    dashboard = Dashboard()
    user = User('test@example.com', 'developer', ['learn python', 'learn java'])
    roadmap = dashboard.redirect(user)
    assert roadmap.weeks == 1
    assert roadmap.goals == ['learn python', 'learn java']
