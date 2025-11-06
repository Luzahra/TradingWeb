"""Pydantic schemas for request and response payloads."""
from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    timezone: str = Field(default="Europe/Berlin", description="IANA timezone string")


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class HoldingBase(BaseModel):
    user_id: int
    ticker: str = Field(..., min_length=1, max_length=20)
    shares: float = Field(..., ge=0)


class HoldingCreate(HoldingBase):
    pass


class HoldingRead(HoldingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class HoldingList(BaseModel):
    holdings: List[HoldingRead]


class NewsRead(BaseModel):
    id: int
    ticker: str
    title: str
    url: str
    published_at: datetime
    summary: Optional[str]

    class Config:
        orm_mode = True


class EventRead(BaseModel):
    id: int
    ticker: str
    type: str
    start_at: datetime
    end_at: Optional[datetime]
    source: Optional[str]

    class Config:
        orm_mode = True
