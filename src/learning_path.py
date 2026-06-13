import json
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Module:
    title: str
    description: str

@dataclass
class LearningPath:
    role: str
    goals: List[str]
    modules: List[Module] = field(default_factory=list)

    def generate_path(self):
        self.modules = [
            Module("Introduction to AI", "Overview of AI technologies and applications."),
            Module("Machine Learning Basics", "Fundamentals of machine learning."),
            Module("Data Science Essentials", "Key concepts in data science."),
            Module("AI Project Management", "Managing AI projects effectively."),
            Module("Advanced Machine Learning", "Deep dive into advanced ML techniques."),
            Module("Data Visualization", "Techniques for visualizing data insights."),
            Module("AI Ethics", "Understanding ethical implications in AI."),
            Module("Future Trends in AI", "Exploring upcoming trends and technologies in AI.")
        ]

    def to_json(self) -> str:
        return json.dumps({
            "role": self.role,
            "goals": self.goals,
            "modules": [module.__dict__ for module in self.modules]
        })
