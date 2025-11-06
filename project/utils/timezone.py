"""Timezone related utilities."""
from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo


def to_timezone(dt: datetime, timezone: str) -> datetime:
    """Convert naive/aware datetime to the specified timezone."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))
    return dt.astimezone(ZoneInfo(timezone))
