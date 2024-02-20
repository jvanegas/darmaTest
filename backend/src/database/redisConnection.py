import aioredis
import os

host = os.getenv("REDIS_HOST", "localhost")
port = os.getenv("REDIS_PORT", "6379")
# TODO: add password to redis connection

redis_url = f'redis://{host}:{port}'

async def get_redis_connection():
    redis = aioredis.from_url(redis_url, encoding="utf-8", decode_responses=True)
    try:
        yield redis
    finally:
        await redis.close()


