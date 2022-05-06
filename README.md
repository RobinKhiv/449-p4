# 449-p4
## SETUP
initialize the databases for "Materializing data from views"</br>

with:
```./bin/init.sh```

## Service to Track State
To run the Fastapi service
use the command:
```foreman start```

Tracking service can be accessed at http://localhost:5001/docs
  
## Materializing Data from Views
1.copy python script winlossstats.py from the project location to /usr/lib/python3/dist-packages using below command

cp winlossstats.py /usr/lib/python3/dist-packages

2. copy the var folder containing sharded dbs to /usr/lib/python3/dist-packages using below command

cp -r  var /usr/lib/python3/dist-packages

3. go inside /usr/lib/python3/dist-packages and run below command

python winlossstats.py

## Scheduling updates with cron
<p>Open terminal on Tuffix.<br>
  Write ```crontab -e```<br>
  scroll to the end<br>
  go to the end of file
  if python file is in root file paste -> `*/10 * * * * /usr/bin/flock -n my-py.lock /usr/bin/python3.8 winlossstats.py` <br>
  if python file is in different folder paste -> `*/10 * * * * cd <path to your python file> && /usr/bin/flock -n my-py.lock /usr/bin/python3.8 winlossstats.py` <br>
  save the file and Done :)<br>

## Pulling Leaderboards from Redis
 1.Go inside 449-p4-main project directory run the command
 
  foreman start
  
 2. The modified service from project 3 can be accessed at http://localhost:5002/docs
  
