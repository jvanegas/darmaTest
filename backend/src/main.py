# Configuration imports
from fastapi import FastAPI, Depends
from src.config import config
import src.utils.logger as logger
from src.database.dbConnection import SessionLocal

# TODO: find better way to import config before modules that depend on env variables already being set
# TODO: 

# App imports
from src.auth.router import router as auth_router

# Create FastAPI instance
app = FastAPI(debug=config["DEBUG"])

# Include routers
# Actually, auth is an already exisiting API in the Darma core app
app.include_router(auth_router, prefix="/auth", tags=["auth"])

logger.get_logger(__name__, config["LOG_LEVEL"]).info("Server up and running!")
