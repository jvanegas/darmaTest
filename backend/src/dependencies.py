import src.utils.logger as logger
from src.database.dbConnection import SessionLocal
from src.config import config

# TODO: Can be imrpoved. I was expectig the DI to work as a plugin, passed to
# all the routers, but it seems that is neede to pass de depedencies to each route.
__logger = logger.get_logger(__name__, config["LOG_LEVEL"]) # If used directly in get_logger, gets called multiple times

# Get logger
def get_logger():
    # TODO: improve __name__ to work only as one logger
    return __logger

# Get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
