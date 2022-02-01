import json
import csv
from csv import DictReader


with open("../File/books.csv", newline='') as b:
    books = DictReader(b)
    bo = []

    for row in books:
        k = {}
        k["Title"] = row["Title"]
        k["Author"] = row["Author"]
        k["Height"] = row["Height"]
        bo.append(dict(k))

with open("../File/users.json", "r") as u:
    users = json.loads(u.read())
    users_List = users
    us = []

if len(bo) < len(users_List) == True:
    for user in users_List:
        s = {}
        s["name"] = user["name"]
        s["gender"] = user["gender"]
        s["address"] = user["address"]
        s["books"] = [bo.pop(0)] if len(bo) > 0 else []
        us.append(s)

else:
    for user in users_List:
        s = {}
        s["name"] = user["name"]
        s["gender"] = user["gender"]
        s["address"] = user["address"]
        s["books"] = [bo.pop(0)]
        us.append(s)


with open("../File/example2.json", "w") as f:
    s = json.dumps(us, indent=4)
    f.write(s)