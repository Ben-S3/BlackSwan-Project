import mysql.connector
import csv
import pandas as pd

#df = pd.read_csv("user_file.csv")
#print(df)


list = [];
cnx = mysql.connector.connect(host="localhost", port=8889, user="root", password="root", database="Blackswan")

with open('user_file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        list.append(row)
        # print(row)

userid = [];
website = [];
displayname = [];


for i in range(1,len(list)):
    userid.append(list[i][1])
    website.append(list[i][2])
    displayname.append(list[i][3])

# print(userid)
print(displayname)



for i in range(len(userid)):
    query = "INSERT INTO Blackswan_table(username, website, displayname) VALUES("\
            + str(userid[i]) +"," + str(website[i]) + "," + str(displayname[i]) + ");"
    cursor.execute(query)
    cursor = cnx.cursor()
    cnx.commit()

