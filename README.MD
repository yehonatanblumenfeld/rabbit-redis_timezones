# you must have python3 installed on your machine 
steps:
- dowload project 
- open rabbit-redis-timezones folder
- inside the folder:
  - run commands on terminal:
    -  pip/pip3 install -r requirements.txt
    -  docker-compose up -d
  
 -  after docker is finished and containers are running:
    -  start the script with the command: python/python3 collect_timezones.py