import requests
from bs4 import BeautifulSoup as BS
import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'jdscrap'

starturl = "https://www.justdial.com/"
service = str(input("\n enter the service : "))
location = str(input("enter the city : "))
url = starturl + location + "/" + service

agent = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)
soup = (BS(page.content, 'html.parser'))
name = list(soup.find_all(class_="lng_cont_name"))
rating = list(soup.find_all(class_="green-box"))
address = list(soup.find_all(class_="cont_fl_addr"))
dictionary = dict()

contacts = list(soup.find_all(class_='contact-info'))

data = dict()
id = 0
for i in contacts:
    numbers = i.find_all(class_="mobilesv")
    data[id] = list()
    for j in numbers:
        if j['class'][1] == "icon-yz":
            temp = 1
        elif j['class'][1] == "icon-wx":
            temp = 2
        elif j['class'][1] == "icon-vu":
            temp = 3
        elif j['class'][1] == "icon-ts":
            temp = 4
        elif j['class'][1] == "icon-rq":
            temp = 5
        elif j['class'][1] == "icon-po":
            temp = 6
        elif j['class'][1] == "icon-nm":
            temp = 7
        elif j['class'][1] == "icon-lk":
            temp = 8
        elif j['class'][1] == "icon-ji":
            temp = 9
        elif j['class'][1] == "icon-acb":
            temp = 0
        if j['class'][1] != "icon-fe" and j['class'][1] != "icon-dc" and j['class'][1] != "icon-hg" and j['class'][
            1] != "icon-ba":
            data[id].append(str(temp))
    id = id + 1

for i in data:
    data[i] = ''.join(map(str, data[i]))

for x in range(10):
    dictionary[x] = dict()
    dictionary[x]["compname"] = name[x].get_text()
    dictionary[x]["rating"] = rating[x].get_text()
    dictionary[x]["address"] = address[x].get_text()
    dictionary[x]["contacts"] = data[x]
    dictionary[x]["city"] = location
    dictionary[x]["service"] = service
print(dictionary)

# icon-yz = 1
# icon-wx = 2
# icon-vu = 3
# icon-ts = 4
# icon-rq = 5
# icon-po = 6
# icon-nm = 7
# icon-lk = 8
# icon-ji = 9ki
# icon-acb = 0
print("Done !!")
x=0
y=0
listof=[["null"]*6]*10
for x in range(len(dictionary)):
    listof[x]=list(dictionary[x].values())
print(listof)


mydb = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)

cursor = mydb.cursor()
sql = "INSERT INTO scrap(compname,rating,address,contacts,city,service) VALUES (%s, %s, %s, %s, %s, %s) "
cursor.executemany(sql,listof)
mydb.commit()
print("done")
