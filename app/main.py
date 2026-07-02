from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger
from app.database.duckdb import get_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Business Discovery Platform")

    conn = get_connection()
    conn.execute("SELECT 1")
    conn.close()

    logger.info("DuckDB initialized")

    yield

    logger.info("Application stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
    }