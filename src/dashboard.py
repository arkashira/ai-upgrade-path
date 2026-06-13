from src.models import User
from src.roadmap import RoadmapGenerator

class Dashboard:
    def __init__(self):
        self.roadmap_generator = RoadmapGenerator()

    def redirect(self, user):
        roadmap = self.roadmap_generator.generate(user)
        # Redirect to dashboard with roadmap
        return roadmap
