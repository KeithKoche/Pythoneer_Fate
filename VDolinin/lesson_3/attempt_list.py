#some_file = open('../files/text_doc.txt')

# f = open("../files/text_doc.txt")
#print(some_file.read())
#some_file.close()

#f = open('../files/text_doc.txt')
#print(f.read())
#f.close()


import json

#json_data = json.loads(open('users.json', encoding="utf8").read())
#print(json_data.count(a))
#users_list = ['users']
#for users in users_list:
#        print(users[balance])
import csv
from csv import DictReader
#
with open("../files/books.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    for row in reader:
        print(row)
#
with open("../files/books.csv", newline='') as f:
#   reader = DictReader(f)
#
#   for row in reader:
#       print(row)




