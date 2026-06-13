import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class Role(Enum):
    DEVELOPER = "developer"
    DESIGNER = "designer"
    PRODUCT_MANAGER = "product_manager"

@dataclass
class User:
    email: str
    role: Role
    goals: List[str]

class Onboarding:
    def __init__(self):
        self.users = {}

    def signup(self, email: str, role: Role, goals: List[str]):
        user = User(email, role, goals)
        self.users[email] = user
        self.save_user(user)
        return self.generate_roadmap(user)

    def generate_roadmap(self, user: User):
        # Simple roadmap generation for demonstration purposes
        roadmap = {
            "week1": [
                {"day1": "Learn about AI"},
                {"day2": "Explore machine learning"},
                {"day3": "Discover deep learning"},
            ]
        }
        return roadmap

    def save_user(self, user: User):
        # Simulate saving user data securely
        with open(f"{user.email}.json", "w") as f:
            json.dump(
                {
                    "email": user.email,
                    "role": user.role.value,
                    "goals": user.goals,
                },
                f,
            )

    def load_user(self, email: str):
        try:
            with open(f"{email}.json", "r") as f:
                user_data = json.load(f)
                return User(user_data["email"], Role(user_data["role"]), user_data["goals"])
        except FileNotFoundError:
            return None
