"""SQLAlchemy ORM models for the portfolio tracker."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    timezone = Column(String(64), nullable=False, default="Europe/Berlin")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    holdings = relationship("Holding", back_populates="user", cascade="all, delete-orphan")
    news_items = relationship("News", back_populates="user", cascade="all, delete-orphan")


class Holding(Base):
    __tablename__ = "holdings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    ticker = Column(String(20), nullable=False, index=True)
    shares = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship("User", back_populates="holdings")


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    ticker = Column(String(20), nullable=False, index=True)
    title = Column(String(512), nullable=False)
    url = Column(String(512), nullable=False)
    published_at = Column(DateTime, nullable=False)
    summary = Column(Text, nullable=True)

    user = relationship("User", back_populates="news_items")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(20), nullable=False, index=True)
    type = Column(String(64), nullable=False)  # e.g. earnings, dividend
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=True)
    source = Column(String(128), nullable=True)
