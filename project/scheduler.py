"""Application scheduler configuration."""
from __future__ import annotations

from datetime import datetime
from typing import Iterable

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import User
from .services.email_service import send_email
from .services.news_fetcher import fetch_latest_news
from .utils.timezone import to_timezone


def send_daily_digest(user_id: int) -> None:
    """Placeholder for sending a daily digest to a user."""
    print(f"Preparing daily digest for user {user_id}")


def _gather_user_tickers(db: Session, user: User) -> Iterable[str]:
    return [holding.ticker for holding in user.holdings]


def _send_digest_for_user(db: Session, user: User) -> None:
    tickers = _gather_user_tickers(db, user)
    news_items = fetch_latest_news(tickers)
    body_lines = [
        f"News for {item.ticker}: {item.summary}" for item in news_items
    ]
    body = "\n".join(body_lines) if body_lines else "No news available today."
    send_email(user.email, "Your daily portfolio digest", body)
    send_daily_digest(user.id)


def run_daily_jobs() -> None:
    """Run daily digest jobs for all users when their local time hits 14:00."""
    db = SessionLocal()
    try:
        users = db.query(User).all()
        now_utc = datetime.utcnow()
        for user in users:
            localized = to_timezone(now_utc, user.timezone)
            if localized.hour == 14:
                _send_digest_for_user(db, user)
    finally:
        db.close()


def start_scheduler() -> BackgroundScheduler:
    """Create and start the APScheduler instance."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        run_daily_jobs,
        CronTrigger(minute=0, timezone="UTC"),
        id="daily_digest_runner",
        replace_existing=True,
    )
    scheduler.start()
    return scheduler
