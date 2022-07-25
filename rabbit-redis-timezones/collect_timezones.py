import requests
import rabbitmq_connection as rabbit
import redis_connection as redis


def main():
    response = requests.get("http://worldtimeapi.org/api/timezone")
    print("Requesting time zones ---------------------->      Done!")
    # time zones list 
    time_zones = response.text.replace('"', "").replace("[", "").replace("]", "").split(",")


    for zone in time_zones:
        response = requests.get(f"http://worldtimeapi.org/api/timezone/{zone}")
        print(f"Requesting time zones detailes for {zone}        ---------------->     (1/3) Done! ")
        timezone_detailes = response.text
    
        # sending data to redis
        redis.insert_to_redis(zone, timezone_detailes)
        print(f"Sending data to redis                               ------------------------>    (2/3)  Done! ")
        # sending data to rabbitmq
        rabbit.publish_message(timezone_detailes)
        print(f"Sending data to rabbitmq                            ------------------------>    (3/3)  Done! ")   
        
         
    print("Timezones collector finished")
    print("rabbitmq console managment on --> http://localhost:15672/")
    print("rabbitmq credentials:\nUser: johnny\npassword:1234")
    print("redis console on --> http://localhost:8081/")
if __name__ == "__main__":
    main()