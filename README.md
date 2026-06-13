# AI Upgrade Path

This project provides a personalized learning path engine for AI professionals. Users can select their role and career goals to generate a tailored learning roadmap.

## Features

- Generate a 4-week roadmap with 2 modules per week based on user-selected role and goals.
- Automatically updates the roadmap when new breakthroughs are added to the knowledge base.
- Users can view, reorder, or skip modules without breaking the path.

## Usage

1. Create an instance of `LearningPath` with the desired role and goals.
2. Call `generate_path()` to create the learning modules.
3. Use `to_json()` to get the learning path in JSON format.

## Running Tests

To run the tests, use the following command:
