import requests
import rabbitmq_connection as rabbit
import redis_connection as redis

def main():
    response = requests.get("http://worldtimeapi.org/api/timezone")

    # time zones list 
    time_zones = response.text.replace('"', "").replace("[", "").replace("]", "").split(",")


    for zone in time_zones:
        response = requests.get(f"http://worldtimeapi.org/api/timezone/{zone}")
        timezone_detailes = response.text
        
        # sending data to redis
        redis.insert_to_redis(zone, timezone_detailes)
        
        # sending data to rabbitmq
        rabbit.publish_message(timezone_detailes)

if __name__ == "__main__":
    main()