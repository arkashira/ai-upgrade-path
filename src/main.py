import argparse
from learning_path import LearningPathEngine


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Upgrade Path")
    parser.add_argument(
        "--role",
        type=str,
        required=True,
        help="Select role (ML Engineer, Data Scientist, AI PM)",
    )
    parser.add_argument(
        "--goals",
        nargs=3,
        required=True,
        help="Select 3 career goals",
    )
    args = parser.parse_args()

    engine = LearningPathEngine()
    learning_path = engine.generate_learning_path(args.role, args.goals)

    print("Learning Path:")
    for i, module in enumerate(learning_path.modules):
        print(f"Week {i // 2 + 1}: {module.name} - {module.description}")


if __name__ == "__main__":
    main()
