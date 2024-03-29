# Configuration imports
from fastapi import FastAPI
from src.config import config
import src.utils.logger as logger

# TODO: find better way to import config before modules that depend on env variables already being set

# App imports
from src.auth.router import router as auth_router
from src.families.router import router as families_router

# Create FastAPI instance
app = FastAPI(debug=config["DEBUG"])

# Include routers
# Actually, auth is an already exisiting API in the Darma core app
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(families_router, prefix="/family", tags=["family"])

logger.get_logger(__name__, config["LOG_LEVEL"]).info("Server up and running!")
