from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Dict, Optional, Set


@dataclass(frozen=True)
class Badge:
    """A badge awarded to a user for completing modules in a topic."""
    name: str
    topic: str
    awarded_at: str  # ISO‑8601 timestamp


@dataclass
class User:
    """Simple user model holding completed modules and earned badges."""
    user_id: str
    # Mapping topic -> set of module identifiers completed
    _completed_modules: Dict[str, Set[str]] = field(default_factory=dict, init=False, repr=False)
    # List of earned badges
    badges: List[Badge] = field(default_factory=list)

    def complete_module(self, topic: str, module_id: str) -> Optional[Badge]:
        """Record completion of a module. Return a Badge if this completion
        triggers an award (i.e., 5 unique modules in the topic)."""
        completed = self._completed_modules.setdefault(topic, set())
        completed.add(module_id)

        # Award badge only once per topic when reaching exactly 5 distinct modules
        if len(completed) == 5:
            badge = Badge(
                name=f"{topic.title()} Expert",
                topic=topic,
                awarded_at=datetime.utcnow().isoformat() + "Z",
            )
            self.badges.append(badge)
            return badge
        return None

    def get_badges(self, topic: Optional[str] = None) -> List[Badge]:
        """Return all badges, optionally filtered by topic."""
        if topic is None:
            return list(self.badges)
        return [b for b in self.badges if b.topic == topic]

    def export_badge(self, badge: Badge) -> str:
        """Export a single badge as a JSON credential."""
        credential = {
            "user_id": self.user_id,
            "badge_name": badge.name,
            "topic": badge.topic,
            "awarded_at": badge.awarded_at,
        }
        return json.dumps(credential, sort_keys=True)
