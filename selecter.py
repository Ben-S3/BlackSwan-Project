# Author: Hope Church
# Date Created: 4/8/2021
# Date updated: 4/8/2021
# Description: inserts objects into database given by parser
import database_objects as dbo #not how you import files, here for reference
import mysql.connector


#please change these credentials & hostname on production
def db_connect():
	print("connecting to database")
	mydb = mysql.connector.connect(
		host="localhost",
		user="root", 
		password="",
		database="blackswan_event_tracker"
	)
	mycursor = mydb.cursor()
	return [mydb, mycursor]

#finding events

def find_events_by_name(name):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	event_statement="SELECT * FROM event WHERE name LIKE '%%%s%%'"
	event_val=(name,)
	mycursor.execute(event_statement, event_val)
	return mycursor.fetchall()

def find_events_by_date(start_date,end_date):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	event_statement="SELECT * FROM event WHERE  date_start BETWEEN  '%s' '%s' OR date_end BETWEEN '%s','%s'"
	event_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(event_statement, event_val)
	return mycursor.fetchall()

def find_event_by_keywords(keywords):
	
	
def find_event_by_keywords_posts(keywords):
	
def find_event_by_location(location):


#finding locations
def find_location_by_post(post):
	
def find_location_by_event(event):
	
	
#finding posts
def find_post_by_event(idevent):
	
def find_post_by_user(iduser):
	
#finding media
	
def find_media_by_post(idpost):

def find_url_by_post(idpost):
	
def find_user_by_post(idpost):
	
def find_user_by_event(idevent):
	
def find_tag_by_event(idevent):
