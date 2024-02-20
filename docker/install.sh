docker compose up -d
docker exec -it docker-redis-1 redis-cli config set notify-keyspace-events KEA