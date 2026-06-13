import json
from src.config import config
from src.models import User

class Auth:
    def __init__(self):
        self.providers = ['email', 'google']

    def signup(self, provider, email, role, goals):
        if provider not in self.providers:
            raise ValueError('Invalid provider')
        user = User(email, role, goals)
        config.data[email] = {'role': role, 'goals': goals}
        config.save()
        return user

    def login(self, email):
        if email in config.data:
            return User(email, config.data[email]['role'], config.data[email]['goals'])
        return None
