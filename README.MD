# you must have python3, docker, docker compose installed on your machine 
steps:
- dowload project 
- open project folder
- inside the folder:
  - run commands on terminal:
    -  pip/pip3 install -r requirements.txt
    -  docker-compose up -d
  
  - after docker is finished and containers are running:
    -  start the script with the command: python/python3 rabbit-redis-timezones\collect_timezones.py