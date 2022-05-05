# Science Fiction Novel API - FastAPI Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#
import uvicorn
from fastapi import FastAPI, Depends, Response, HTTPException, status
import redis

redisClient = redis.StrictRedis(host='localhost',
                                port=6379,
                                db=0)


# Uncomment below line to test without traefik
app = FastAPI()
# Uncomment below line to test with traefik
# app = FastAPI(root_path="/api/v1")



# get top10 records for user wins from redis
@app.get("/stats/top10wins")
def get_top10users():
    return {"Top 10 users by number of wins are": redisClient.zrange("winleaders", 0, 9, desc=True)}


# get top10 records for user streaks from redis
@app.get("/stats/top10streaks")
def get_top10users():
    return {"Top 10 users by number of streaks are": redisClient.zrange("streaksleaders", 0, 9, desc=True)}



if __name__ == "__main__":
    uvicorn.run("ModifiedProj3StatsService:app", host="0.0.0.0", port=5001, log_level="info")