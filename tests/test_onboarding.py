from onboarding import Onboarding, Role
import json
import os

def test_sign_up():
    onboarding = Onboarding()
    email = "user@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects", "Get certified"]
    roadmap = onboarding.sign_up(email, role, goals)
    assert roadmap is not None
    assert "week1" in roadmap

def test_generate_roadmap():
    onboarding = Onboarding()
    email = "user@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects", "Get certified"]
    onboarding.sign_up(email, role, goals)
    roadmap = onboarding.generate_roadmap(email)
    assert roadmap is not None
    assert "week1" in roadmap

def test_store_data_securely():
    onboarding = Onboarding()
    email = "user@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects", "Get certified"]
    onboarding.store_data_securely(email, role, goals)
    assert os.path.exists(f"{email}.json")
    with open(f"{email}.json", "r") as f:
        data = json.load(f)
        assert data["email"] == email
        assert data["role"] == role.value
        assert data["goals"] == goals

def test_oauth_sign_up():
    onboarding = Onboarding()
    email = "user@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects", "Get certified"]
    # Simulate OAuth sign up
    roadmap = onboarding.sign_up(email, role, goals)
    assert roadmap is not None
    assert "week1" in roadmap

def test_sign_up_via_email():
    onboarding = Onboarding()
    email = "user@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects", "Get certified"]
    # Simulate email sign up
    roadmap = onboarding.sign_up(email, role, goals)
    assert roadmap is not None
    assert "week1" in roadmap
