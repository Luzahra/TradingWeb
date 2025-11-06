"""CRUD operations for user entities."""
from __future__ import annotations

from sqlalchemy.orm import Session

from .. import models, schemas


def get_user_by_email(db: Session, email: str) -> models.User | None:
    """Return a user by email if it exists."""
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user_in: schemas.UserCreate) -> models.User:
    """Create a new user with the supplied data."""
    user = models.User(email=user_in.email, timezone=user_in.timezone)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
