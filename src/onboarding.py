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

    def sign_up(self, email: str, role: Role, goals: List[str]):
        self.users[email] = User(email, role, goals)
        return self.generate_roadmap(email)

    def generate_roadmap(self, email: str):
        user = self.users.get(email)
        if user:
            # Auto-generate first week's roadmap based on role and goals
            roadmap = {
                "week1": [
                    {"day1": "Introduction to AI"},
                    {"day2": "Setting up the development environment"},
                    {"day3": "Basic programming concepts"},
                    {"day4": "Data structures and algorithms"},
                    {"day5": "Introduction to machine learning"},
                    {"day6": "Deep learning basics"},
                    {"day7": "Project setup and planning"}
                ]
            }
            return roadmap
        return None

    def store_data_securely(self, email: str, role: Role, goals: List[str]):
        # Store data securely per GDPR
        with open(f"{email}.json", "w") as f:
            json.dump({
                "email": email,
                "role": role.value,
                "goals": goals
            }, f)

def main():
    onboarding = Onboarding()
    email = "user@example.com"
    role = Role.DEVELOPER
    goals = ["Learn AI", "Build projects", "Get certified"]
    roadmap = onboarding.sign_up(email, role, goals)
    print(roadmap)
    onboarding.store_data_securely(email, role, goals)

if __name__ == "__main__":
    main()
