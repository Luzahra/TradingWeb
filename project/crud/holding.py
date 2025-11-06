"""CRUD operations for holdings."""
from __future__ import annotations

from typing import List

from sqlalchemy.orm import Session

from .. import models, schemas


def create_holding(db: Session, holding_in: schemas.HoldingCreate) -> models.Holding:
    """Create a holding for a user."""
    holding = models.Holding(
        user_id=holding_in.user_id, ticker=holding_in.ticker.upper(), shares=holding_in.shares
    )
    db.add(holding)
    db.commit()
    db.refresh(holding)
    return holding


def get_holdings_for_user(db: Session, user_id: int) -> List[models.Holding]:
    """Return all holdings for a given user."""
    return db.query(models.Holding).filter(models.Holding.user_id == user_id).all()


def delete_holding(db: Session, holding_id: int) -> bool:
    """Delete a holding by its identifier."""
    holding = db.query(models.Holding).filter(models.Holding.id == holding_id).first()
    if not holding:
        return False
    db.delete(holding)
    db.commit()
    return True
