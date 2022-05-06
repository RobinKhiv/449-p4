# 449-p4

## Service to Track State
To run the Fastapi service
use the command:
```foreman start```

## Materializing Data from Views

## Scheduling updates with cron
<p>Open terminal on Tuffix.<br>
  Write ```crontab -e```<br>
  scroll to the end<br>
  go to the end of file
  if python file is in root file paste -> ```*/10 * * * * /usr/bin/flock -n my-py.lock /usr/bin/python3.8 winlossstats.py```<br>
  if python file is in different folder paste -> ```*/10 * * * * cd <path to your python file> && /usr/bin/flock -n my-py.lock /usr/bin/python3.8 winloassstats.py```<br>
  save the file and Done :)<br>

## Pulling Leaderboards from Redis
