#Прочитать файл .csv, выбрать нужные столбцы, вывести их
#import csv
#file = open('../files/books.csv')
#reader = csv.reader(file)
#data = list(reader)
#for data in data:
#    print(data[0], '<--- тут название книги', ' | ', 'а здесь издательство --->', data[4])
#    file.close()

#Выбрать уникальные символы из файла
#file = set('trollololololo')
#print(file)

#Проверить, есть ли в файле искомое значение
#days = set(["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])
#print("Monday" in days)


#Разделить файл построчно по 1 книге
#import csv
#from csv import DictReader


#with open("../files/books.csv", newline='') as file:
#    reader = DictReader(file)
#    for row in reader:
#        print(row)


#Вывести айди и возраст пользователей
import json

with open("users.json", "r") as file:
    users = json.loads(file.read())

    users_list = users['users']

for user in users_list:
    print(user["_id"])








