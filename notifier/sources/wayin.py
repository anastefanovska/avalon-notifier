from __future__ import annotations

import re

from ..http import DEFAULT_TIMEOUT, session
from ..source import Event

PAGE_URL = "https://wayin.mk/shop/events"
BASE_URL = "https://wayin.mk"

EVENT_LINK_RE = re.compile(r'href="(/shop/events/[a-z0-9-]+)"', re.IGNORECASE)


class WayInSource:
    key = "wayin"
    display_name = "wayin.mk"

    def fetch(self) -> list[Event]:
        with session() as s:
            response = s.get(PAGE_URL, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
            html = response.text

        seen_paths: set[str] = set()
        events: list[Event] = []
        for match in EVENT_LINK_RE.finditer(html):
            path = match.group(1)
            if path in seen_paths:
                continue
            seen_paths.add(path)
            slug = path.rsplit("/", 1)[-1]
            events.append(Event(id=slug, url=f"{BASE_URL}{path}"))
        return events
