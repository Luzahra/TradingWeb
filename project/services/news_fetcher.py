"""Service layer for retrieving financial news."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List


@dataclass(slots=True)
class NewsItem:
    """Simple container for news results."""

    ticker: str
    title: str
    url: str
    published_at: datetime
    summary: str | None


def fetch_latest_news(tickers: Iterable[str]) -> List[NewsItem]:
    """Fetch the latest news for provided tickers.

    This function is a placeholder for integrating with a real news API.
    """

    news: List[NewsItem] = []
    timestamp = datetime.utcnow()
    for ticker in tickers:
        news.append(
            NewsItem(
                ticker=ticker,
                title=f"Daily summary for {ticker}",
                url="https://example.com/news",
                published_at=timestamp,
                summary=f"Summary for {ticker} at {timestamp.isoformat()}",
            )
        )
    return news
