"""API routes related to holdings management."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas
from ..crud import holding as holding_crud
from ..database import get_db

router = APIRouter(prefix="/holdings", tags=["holdings"])


@router.post("", response_model=schemas.HoldingRead, status_code=status.HTTP_201_CREATED)
def create_holding(
    holding_in: schemas.HoldingCreate, db: Session = Depends(get_db)
) -> schemas.HoldingRead:
    """Create a new holding for a user."""
    holding = holding_crud.create_holding(db, holding_in)
    return holding


@router.get("/{user_id}", response_model=schemas.HoldingList)
def list_holdings(user_id: int, db: Session = Depends(get_db)) -> schemas.HoldingList:
    """Retrieve all holdings for a given user."""
    holdings = holding_crud.get_holdings_for_user(db, user_id)
    return schemas.HoldingList(holdings=holdings)


@router.delete("/{holding_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_holding(holding_id: int, db: Session = Depends(get_db)) -> None:
    """Delete a holding by id."""
    deleted = holding_crud.delete_holding(db, holding_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Holding not found")
    return None
