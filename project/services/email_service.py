"""Email delivery helpers."""
from __future__ import annotations

from typing import Iterable, Optional


def send_email(recipient: str, subject: str, body: str, attachments: Optional[Iterable[tuple[str, str]]] = None) -> None:
    """Placeholder email sender.

    Args:
        recipient: Email address to deliver to.
        subject: Subject of the email.
        body: Plain text body.
        attachments: Optional iterable of (filename, content) tuples.
    """

    print(f"Sending email to {recipient}: {subject}")  # Replace with real implementation
    if attachments:
        for filename, _ in attachments:
            print(f" -> with attachment: {filename}")
