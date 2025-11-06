"""Calendar integration helpers."""
from __future__ import annotations

from datetime import datetime


def generate_ics_event(ticker: str, datetime_start: datetime, title: str, url: str) -> str:
    """Generate a minimal ICS event for a financial calendar item."""
    dtstamp = datetime_start.strftime("%Y%m%dT%H%M%SZ")
    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//PortfolioTracker//EN
BEGIN:VEVENT
UID:{ticker}-{dtstamp}@portfolio-tracker
DTSTAMP:{dtstamp}
DTSTART:{dtstamp}
SUMMARY:{title}
DESCRIPTION:{url}
END:VEVENT
END:VCALENDAR
"""
    return ics_content
