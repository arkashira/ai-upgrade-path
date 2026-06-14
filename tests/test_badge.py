import json
from badge import BadgeManager

def test_award_badge():
    manager = BadgeManager()
    manager.add_module("topic1", "module1")
    manager.add_module("topic1", "module2")
    manager.add_module("topic1", "module3")
    manager.add_module("topic1", "module4")
    manager.add_module("topic1", "module5")
    manager.award_badge("user1", "topic1")
    assert len(manager.get_badges("user1")) == 1

def test_filter_badges():
    manager = BadgeManager()
    manager.add_module("topic1", "module1")
    manager.add_module("topic1", "module2")
    manager.add_module("topic1", "module3")
    manager.add_module("topic1", "module4")
    manager.add_module("topic1", "module5")
    manager.award_badge("user1", "topic1")
    manager.add_module("topic2", "module6")
    manager.add_module("topic2", "module7")
    manager.add_module("topic2", "module8")
    manager.add_module("topic2", "module9")
    manager.add_module("topic2", "module10")
    manager.award_badge("user2", "topic2")
    badges = manager.filter_badges("topic1")
    assert len(badges) == 1
    assert badges[0]["topic"] == "topic1"

def test_export_badges():
    manager = BadgeManager()
    manager.add_module("topic1", "module1")
    manager.add_module("topic1", "module2")
    manager.add_module("topic1", "module3")
    manager.add_module("topic1", "module4")
    manager.add_module("topic1", "module5")
    manager.award_badge("user1", "topic1")
    badges = manager.export_badges("user1")
    assert json.loads(badges) == [{"topic": "topic1", "modules": ["module1", "module2", "module3", "module4", "module5"]}]
