import redis

try: 
    # creating redis connection
    redis_connection = redis.Redis(host='localhost', port=6379)
except Exception as e:
    print("Error occurred in redis connection: " + str(e))
    exit()

# inserting key&value into redis
def insert_to_redis(key: str, value: str):
    try: 
        redis_connection.set(key, value)
    except Exception as e:
        print("Error occurred in insert_to_redis: " + str(e))
    