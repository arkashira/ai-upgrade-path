import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Module:
    name: str
    description: str

@dataclass
class LearningPath:
    role: str
    goals: list
    modules: list

class LearningPathEngine:
    def __init__(self):
        self.knowledge_base = {
            "ML Engineer": [
                Module("Introduction to ML", "Learn the basics of machine learning"),
                Module("Deep Learning", "Learn about deep learning techniques"),
                Module("Natural Language Processing", "Learn about NLP techniques"),
                Module("Computer Vision", "Learn about computer vision techniques"),
                Module("Reinforcement Learning", "Learn about reinforcement learning techniques"),
                Module("Unsupervised Learning", "Learn about unsupervised learning techniques"),
                Module("Supervised Learning", "Learn about supervised learning techniques"),
                Module("Time Series Analysis", "Learn about time series analysis techniques"),
            ],
            "Data Scientist": [
                Module("Introduction to Data Science", "Learn the basics of data science"),
                Module("Data Preprocessing", "Learn about data preprocessing techniques"),
                Module("Data Visualization", "Learn about data visualization techniques"),
                Module("Machine Learning", "Learn about machine learning techniques"),
                Module("Statistics", "Learn about statistical techniques"),
                Module("Data Mining", "Learn about data mining techniques"),
                Module("Big Data", "Learn about big data techniques"),
                Module("Cloud Computing", "Learn about cloud computing techniques"),
            ],
            "AI PM": [
                Module("Introduction to AI", "Learn the basics of artificial intelligence"),
                Module("AI Strategy", "Learn about AI strategy techniques"),
                Module("AI Ethics", "Learn about AI ethics techniques"),
                Module("AI Governance", "Learn about AI governance techniques"),
                Module("AI Risk Management", "Learn about AI risk management techniques"),
                Module("AI Project Management", "Learn about AI project management techniques"),
                Module("AI Team Management", "Learn about AI team management techniques"),
                Module("AI Stakeholder Management", "Learn about AI stakeholder management techniques"),
            ],
        }

    def generate_learning_path(self, role, goals):
        modules = self.knowledge_base[role]
        learning_path = LearningPath(role, goals, [])
        for i in range(4):
            week_modules = []
            for j in range(2):
                if i * 2 + j < len(modules):
                    week_modules.append(modules[i * 2 + j])
            learning_path.modules.append(week_modules)
        return learning_path

    def update_learning_path(self, learning_path, new_breakthrough):
        learning_path.modules.append([new_breakthrough])

    def reorder_modules(self, learning_path, week, module_index, new_module_index):
        week_modules = learning_path.modules[week]
        module = week_modules.pop(module_index)
        week_modules.insert(new_module_index, module)

    def skip_module(self, learning_path, week, module_index):
        week_modules = learning_path.modules[week]
        week_modules.pop(module_index)
