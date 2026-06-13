import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List


@dataclass
class Module:
    name: str
    description: str


@dataclass
class LearningPath:
    role: str
    goals: List[str]
    modules: List[Module]


class LearningPathEngine:
    def __init__(self):
        self.knowledge_base = {
            "ML Engineer": [
                Module("Introduction to ML", "Learn the basics of machine learning"),
                Module("Deep Learning", "Dive into deep learning concepts"),
                Module("Natural Language Processing", "Explore NLP techniques"),
                Module("Computer Vision", "Learn about computer vision applications"),
                Module("Reinforcement Learning", "Discover reinforcement learning"),
                Module("Unsupervised Learning", "Understand unsupervised learning"),
                Module("Supervised Learning", "Master supervised learning"),
                Module("ML Engineering Best Practices", "Learn best practices for ML engineering"),
            ],
            "Data Scientist": [
                Module("Data Preprocessing", "Learn data preprocessing techniques"),
                Module("Data Visualization", "Master data visualization tools"),
                Module("Statistical Analysis", "Understand statistical analysis concepts"),
                Module("Machine Learning", "Apply machine learning to data science"),
                Module("Data Mining", "Explore data mining techniques"),
                Module("Big Data", "Learn about big data processing"),
                Module("Data Storytelling", "Discover data storytelling techniques"),
                Module("Data Science Best Practices", "Learn best practices for data science"),
            ],
            "AI PM": [
                Module("Introduction to AI", "Learn the basics of artificial intelligence"),
                Module("AI Strategy", "Develop an AI strategy for your organization"),
                Module("AI Project Management", "Master AI project management techniques"),
                Module("AI Ethics", "Understand AI ethics and bias"),
                Module("AI Explainability", "Learn about AI explainability techniques"),
                Module("AI Adoption", "Discover AI adoption strategies"),
                Module("AI Governance", "Understand AI governance and compliance"),
                Module("AI PM Best Practices", "Learn best practices for AI project management"),
            ],
        }

    def generate_learning_path(self, role: str, goals: List[str]) -> LearningPath:
        """Create a learning path for the given role and goals."""
        modules = list(self.knowledge_base[role])  # copy to avoid external mutation
        return LearningPath(role, goals, modules)

    def update_learning_path(self, learning_path: LearningPath) -> LearningPath:
        """
        Update the learning path based on new breakthroughs in the knowledge base.
        For simplicity, this example just returns the original learning path unchanged.
        """
        return learning_path

    def reorder_modules(self, learning_path: LearningPath, new_module_order: List[int]) -> LearningPath:
        """
        Return a new LearningPath with modules reordered according to ``new_module_order``.
        The original ``learning_path`` is left untouched.
        """
        reordered = [learning_path.modules[i] for i in new_module_order]
        return LearningPath(learning_path.role, learning_path.goals, reordered)

    def skip_module(self, learning_path: LearningPath, module_index: int) -> LearningPath:
        """
        Return a new LearningPath with the module at ``module_index`` removed.
        """
        remaining = [m for idx, m in enumerate(learning_path.modules) if idx != module_index]
        return LearningPath(learning_path.role, learning_path.goals, remaining)
