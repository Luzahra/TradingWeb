"""FastAPI application entry point."""
from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from .database import Base, engine
from .routers import holding_routes, user_routes
from .scheduler import start_scheduler

load_dotenv()
logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown tasks."""
    Base.metadata.create_all(bind=engine)
    scheduler = start_scheduler()
    try:
        yield
    finally:
        scheduler.shutdown(wait=False)


app = FastAPI(title="Portfolio Tracker API", lifespan=lifespan)
app.include_router(user_routes.router)
app.include_router(holding_routes.router)
