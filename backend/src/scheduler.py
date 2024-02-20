import redis
from config import config
import os

host = os.getenv("REDIS_HOST", "localhost")
port = os.getenv("REDIS_PORT", "6379")

def event_handler(msg): # pragma: no cover
    print(msg)

print(f"Connecting to Redis at {host}:{port}")
conn = redis.Redis(host, port, decode_responses=True, encoding="utf-8")
pubsub = conn.pubsub()
# Harcoded database 0
pubsub.psubscribe(**{"__keyevent@0__:expired": event_handler})
pubsub.run_in_thread(sleep_time=0.01)
