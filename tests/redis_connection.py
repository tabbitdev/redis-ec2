import redis

def check_redis_health():
    try:
        # Connect to Redis
        r = redis.Redis(
            host='23.22.40.39',  # The IP address of your Redis server
            port=6379,  # The port your Redis server is running on
            password='mypassword',  # The password set for your Redis server
            decode_responses=True
        )

        # Ping the Redis server
        if r.ping():
            print('Redis is up and running!')
        else:
            print('Ping failed! Redis might be down.')
    except redis.ConnectionError as e:
        print('Could not connect to Redis:', e)

if __name__ == '__main__':
    check_redis_health()
