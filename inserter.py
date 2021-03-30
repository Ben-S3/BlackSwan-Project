# Author: Hope Church
# Date Created: 3/27/2021
# Date updated: 3/28/2021
# Description: inserts objects into database given by parser
import database_objects.py #not how you import files, here for reference
import mysql.connector



#insert example
#statement="INSERT INTO user (username,website,displayname) VALUES ( %s,%s, %s)"
#val=(user.username,user.website,user.displayname)
#mycursor.execute(statement, val)

#how to get the primary key of the previous transaction:
#mycursor.lastrowid

def stage_one(location,event,tag): #inserts location, event, and tag, and returns a tuple [idlocation,idevent,idtag] order is location > event > tag
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	#insert location
	#get idlocation
	#set event.idlocation=idlocation
	#insert event
	#get idevent
	#set event.idevent=idevent
	#insert tag
	#get idtag
	#set tag.idtag=idevent
	#insert tagevent
	mydb.commit()

def stage_two(idevent, media, url, user, post,location): #inserts media, url, user, location, and post. order is location > user > post > url > media, returns nothing
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	#insert location
	#get idlocation
	#insert user
	#get iduser
	#set post.iduser=iduser
	#insert post
	#get idpost
	#insert url
	#get idurl
	#insert media
	#get idmedia
	#insert media_post
	#insert postevent
	#insert url_post
	mydb.commit()
	
#please change these credentials & hostname on production
def db_connect():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root", 
		password="",
		database="blackswan_event_tracker"
	)
	mycursor = mydb.cursor()
	return [mydb, mycursor]

