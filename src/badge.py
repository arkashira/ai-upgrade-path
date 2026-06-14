import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Badge:
    topic: str
    modules: List[str]

class BadgeManager:
    def __init__(self):
        self.badges = {}
        self.modules = {}

    def add_module(self, topic: str, module: str):
        if topic not in self.modules:
            self.modules[topic] = []
        self.modules[topic].append(module)

    def award_badge(self, user: str, topic: str):
        if topic in self.modules and len(self.modules[topic]) >= 5:
            if user not in self.badges:
                self.badges[user] = []
            self.badges[user].append(Badge(topic, self.modules[topic][:5]))

    def get_badges(self, user: str) -> List[Dict]:
        if user in self.badges:
            return [{"topic": badge.topic, "modules": badge.modules} for badge in self.badges[user]]
        return []

    def filter_badges(self, topic: str) -> List[Dict]:
        badges = []
        for user, user_badges in self.badges.items():
            for badge in user_badges:
                if badge.topic == topic:
                    badges.append({"user": user, "topic": badge.topic, "modules": badge.modules})
        return badges

    def export_badges(self, user: str):
        badges = self.get_badges(user)
        return json.dumps(badges)
