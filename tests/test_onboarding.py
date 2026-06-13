from onboarding import Onboarding, Role, User
import pytest
import os

def test_signup():
    onboarding = Onboarding()
    email = "test@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects"]
    roadmap = onboarding.signup(email, role, goals)
    assert roadmap == {
        "week1": [
            {"day1": "Learn about AI"},
            {"day2": "Explore machine learning"},
            {"day3": "Discover deep learning"},
        ]
    }
    assert os.path.exists(f"{email}.json")

def test_load_user():
    onboarding = Onboarding()
    email = "test@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects"]
    onboarding.signup(email, role, goals)
    loaded_user = onboarding.load_user(email)
    assert loaded_user.email == email
    assert loaded_user.role == role
    assert loaded_user.goals == goals

def test_save_user():
    onboarding = Onboarding()
    email = "test@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects"]
    user = User(email, role, goals)
    onboarding.save_user(user)
    assert os.path.exists(f"{email}.json")

def test_generate_roadmap():
    onboarding = Onboarding()
    email = "test@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects"]
    user = User(email, role, goals)
    roadmap = onboarding.generate_roadmap(user)
    assert roadmap == {
        "week1": [
            {"day1": "Learn about AI"},
            {"day2": "Explore machine learning"},
            {"day3": "Discover deep learning"},
        ]
    }
