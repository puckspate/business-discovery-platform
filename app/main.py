from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger
from app.database.duckdb import get_connection

from app.routers.companies import router as company_router
from app.routers.discoveries import router as discovery_router
from app.routers.documents import router as document_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Business Discovery Platform")

    from app.database.init_db import initialize_database
    initialize_database()

    logger.info("DuckDB initialized")

    yield

    logger.info("Application stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(company_router)
app.include_router(discovery_router)
app.include_router(document_router)

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