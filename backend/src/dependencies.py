import aioredis
import src.utils.logger as logger
from src.config import config
from src.database.dbConnection import SessionLocal
from src.database.redisConnection import redis_url
from fastapi import HTTPException, Header
from src.auth.services import valid_token

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

# There should be a better way to handle this connection in a separate file
async def get_redis_connection():
    redis = aioredis.from_url(redis_url, encoding="utf-8", decode_responses=True)
    try:
        yield redis
    finally:
        await redis.close()

# Validate and decode JWT
def validate_jwt (authorization: str = Header(...)):
  token = authorization.split()[1]

  [valid, decoded_token] = valid_token(token)
  if not valid:
    raise HTTPException(status_code=401, detail="Invalid token")

  return decoded_token
