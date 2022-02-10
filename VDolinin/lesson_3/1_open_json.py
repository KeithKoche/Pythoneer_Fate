import json
from csv import DictReader

with open("../files/books.csv", newline='') as g:
    reader = DictReader(g)
    books = []


    for row in reader:
        tit = {}
        tit["Title"] = row["Title"]
        tit["Author"] = row["Author"]
        tit["Height"] = row["Height"]
        books.append(dict(tit))

with open("../files/users.json") as f:
    users = json.loads(f.read())
    us = users
    aa = []

if len(books) < len(us) == True:
    for user in us:
        ccc = {}
        ccc["name"] = user["name"]
        ccc["gender"] = user["gender"]
        ccc["address"] = user["address"]
        ccc["books"] = [books.pop(0)] if len(books) > 0 else []
        aa.append(ccc)

else:
    for user in us:
        ccc = {}
        ccc["name"] = user["name"]
        ccc["gender"] = user["gender"]
        ccc["address"] = user["address"]
        ccc["books"] = [books.pop(0)]
        aa.append(ccc)

with open("ccaaaa.json", "w") as file:
    rrr = json.dumps(aa, indent=4)
    file.write(rrr)



