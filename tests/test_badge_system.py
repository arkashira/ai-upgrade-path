import json
from datetime import datetime, timezone
import pytest
from badge_system import User, Badge

@pytest.fixture
def user():
    return User(user_id="u123")

def test_badge_awarded_after_five_modules(user):
    topic = "python"
    # Complete four modules – no badge yet
    for i in range(1, 5):
        badge = user.complete_module(topic, f"mod{i}")
        assert badge is None
        assert len(user.badges) == 0

    # Fifth module triggers badge
    badge = user.complete_module(topic, "mod5")
    assert isinstance(badge, Badge)
    assert badge.topic == topic
    assert badge.name == "Python Expert"
    assert len(user.badges) == 1

def test_badge_appears_on_profile(user):
    topic = "ml"
    for i in range(5):
        user.complete_module(topic, f"m{i}")
    assert any(b.topic == topic for b in user.badges)

def test_export_json_credential(user):
    topic = "data"
    for i in range(5):
        user.complete_module(topic, f"d{i}")
    badge = user.get_badges(topic)[0]
    cred_json = user.export_badge(badge)
    data = json.loads(cred_json)

    assert data["user_id"] == "u123"
    assert data["badge_name"] == "Data Expert"
    assert data["topic"] == topic

    # Validate timestamp format (ISO‑8601 UTC)
    dt = datetime.fromisoformat(data["awarded_at"].replace("Z", "+00:00"))
    assert dt.tzinfo == timezone.utc

def test_filter_badges_by_topic(user):
    topics = ["go", "rust"]
    for t in topics:
        for i in range(5):
            user.complete_module(t, f"{t}{i}")

    go_badges = user.get_badges("go")
    rust_badges = user.get_badges("rust")
    all_badges = user.get_badges()

    assert len(go_badges) == 1 and go_badges[0].topic == "go"
    assert len(rust_badges) == 1 and rust_badges[0].topic == "rust"
    assert len(all_badges) == 2
