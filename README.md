<h3 align="center">🛠️ ai-upgrade-path</h3>

<div align="center">
  <img src="https://img.shields.io/github/license/axentx/ai-upgrade-path" alt="License: MIT">
  <img src="https://img.shields.io/badge/language-Python%203.11-blue" alt="Python 3.11">
  <img src="https://img.shields.io/github/actions/workflow/status/axentx/ai-upgrade-path/ci.yml?branch=main" alt="Build Status">
  <img src="https://img.shields.io/github/stars/axentx/ai-upgrade-path?style=social" alt="GitHub stars">
</div>

---

# 🚀 ai-upgrade-path

**Power tech professionals with continuous AI learning.**  
A platform that curates, personalises and delivers the latest AI knowledge so developers stay ahead of the curve.

## Why ai-upgrade-path?

- **Curated content** – 100 % AI‑generated learning paths, updated every 24 h.
- **Personalised pacing** – Adaptive quizzes that adjust difficulty in real time.
- **Skill gap analytics** – Visual dashboards showing progress vs industry benchmarks.
- **Built for developers** – Integrates with GitHub, VS Code and Slack for in‑context learning.
- **Zero friction** – One‑click install, no heavy dependencies.
- **Open‑source** – MIT licence, community‑driven roadmap.

## Feature Overview

| Feature | Description |
|---------|-------------|
| 📚 Learning Paths | AI‑generated sequences of articles, videos and exercises. |
| 🎯 Skill Assessments | Adaptive quizzes that adapt to your proficiency. |
| 📊 Progress Dashboard | Visualise your skill growth against peers. |
| 🔗 Integrations | GitHub, VS Code, Slack, and more. |
| 🛠️ CLI Tool | Manage paths, sync progress and export reports. |

## Tech Stack

- Python 3.11
- Poetry (dependency management)
- Pytest (testing)
- FastAPI (optional backend for future extensions)
- SQLite (local persistence)
- GitHub Actions (CI/CD)

## Project Structure

```
ai-upgrade-path/
├── business/          # Business logic and domain models
├── src/               # Core application code
├── tests/             # Unit and integration tests
├── pyproject.toml     # Poetry configuration
├── requirements.txt   # Pin of runtime dependencies
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/ai-upgrade-path.git
cd ai-upgrade-path

# Install dependencies with Poetry
poetry install

# Run the CLI tool
poetry run ai-upgrade-path --help
```

## Deploy

The project is a pure Python CLI, so deployment is simply packaging:

```bash
# Build a wheel
poetry build

# Publish to PyPI (requires credentials)
poetry publish
```

## Status

Active development – last commit `82a6bdb` (2026‑06‑10). The core CLI and learning‑path generator are fully functional.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT © Axentx