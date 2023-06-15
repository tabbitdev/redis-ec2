version: '3'
services:
  redis:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "6379:6379"
    networks:
      - backend
    command: redis-server /data/redis.conf

networks:
  backend:
    driver: bridge
