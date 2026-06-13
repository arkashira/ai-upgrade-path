import pytest
from src.auth import Auth

def test_signup():
    auth = Auth()
    user = auth.signup('email', 'test@example.com', 'developer', ['learn python', 'learn java'])
    assert user.email == 'test@example.com'
    assert user.role == 'developer'
    assert user.goals == ['learn python', 'learn java']

def test_login():
    auth = Auth()
    auth.signup('email', 'test@example.com', 'developer', ['learn python', 'learn java'])
    user = auth.login('test@example.com')
    assert user.email == 'test@example.com'
    assert user.role == 'developer'
    assert user.goals == ['learn python', 'learn java']
