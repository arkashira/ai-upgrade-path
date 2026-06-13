from src.models import Roadmap, User

class RoadmapGenerator:
    def generate(self, user: User):
        return Roadmap(1, user.goals)
