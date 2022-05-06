# Science Fiction Novel API - FastAPI Edition


#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#


import sqlite3
import redis

r = redis.StrictRedis(host='localhost',
                                port=6379,
                                db=0)

GAMEDB1 = "./var/game1.db"
GAMEDB2 = "./var/game2.db"
GAMEDB3 = "./var/game3.db"

def get_top10WinRecordsFromShard1(
):
    con = sqlite3.connect(GAMEDB1)
    cur = con.execute("select user_id,wins from wins limit 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10WinRecordsFromShard2(
):
    con = sqlite3.connect(GAMEDB2)
    cur = con.execute("select user_id,wins from wins limit 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10WinRecordsFromShard3(
):
    con = sqlite3.connect(GAMEDB3)
    cur = con.execute("select user_id,wins from wins limit 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10usersBasedonWins():
    combined_records = {}
    combined_records.update(get_top10WinRecordsFromShard1())
    combined_records.update(get_top10WinRecordsFromShard2())
    combined_records.update(get_top10WinRecordsFromShard3())
    r.zadd("winleaders", combined_records)
    print(r.zrange("winleaders", 0, -1,desc=True))

def get_top10StreaksRecordsFromShard1(
):
    con = sqlite3.connect(GAMEDB1)
    cur = con.execute("select user_id,streak from streaks order by streak desc LIMIT 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10StreaksRecordsFromShard2(
):
    con = sqlite3.connect(GAMEDB2)
    cur = con.execute("select user_id,streak from streaks order by streak desc LIMIT 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10StreaksRecordsFromShard3(
):
    con = sqlite3.connect(GAMEDB3)
    cur = con.execute("select user_id,streak from streaks order by streak desc LIMIT 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10usersBasedonStreaks():
    combined_records = {}
    combined_records.update(get_top10StreaksRecordsFromShard1())
    combined_records.update(get_top10StreaksRecordsFromShard2())
    combined_records.update(get_top10StreaksRecordsFromShard3())
    r.zadd("streaksleaders", combined_records)
    print(r.zrange("streaksleaders", 0, -1,desc=True))

if __name__ == '__main__':
    get_top10usersBasedonWins()
    get_top10usersBasedonStreaks()


