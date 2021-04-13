# Author: Hope Church
# Date Created: 4/8/2021
# Date updated: 4/8/2021
# Description: selects objects for the UI
import database_objects as dbo 
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
	events=[]
	event_statement="SELECT id,name,date_start,time_start,date_end,time_end,idlocation FROM event WHERE name LIKE '%%%s%%'"
	event_val=(name,)
	mycursor.execute(event_statement, event_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		events.append(tuple_to_event(i))
	return events


def find_events_by_date(start_date,end_date):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	event_statement="""SELECT id,name,date_start,time_start,date_end,time_end,idlocation 
					FROM event 
					WHERE  date_start BETWEEN  '%s' '%s' OR date_end BETWEEN '%s','%s'"""
	event_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(event_statement, event_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		events.append(tuple_to_event(i))
	return events

def find_event_by_keywords(keywords):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	for i in keywords:
		event_statement="""SELECT event.id,event.name,event.date_start,event.time_start,event.date_end,event.time_end,event.idlocation 
						FROM event e,tag t,tagevent te 
						WHERE  e.id=te.idevent AND t.id=te.idtag AND t.name LIKE '%%%s%%'"""
		event_val=(start_date,end_date,start_date,end_date,)
		mycursor.execute(event_statement, event_val)
		tuples=mycursor.fetchall()
		for i in tuples:
			events.append(tuple_to_event(i))
	return events

def find_event_by_keywords_in_posts(keywords):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	for i in keywords:
		event_statement="""SELECT event.id,event.name,event.date_start,event.time_start,event.date_end,event.time_end,event.idlocation 
						FROM event e, postevent pe, post p
						WHERE  e.id=pe.idevent AND p.id=pe.idPost AND (post.title LIKE '%%%s%%' OR post.description LIKE '%%%s%%')"""
		event_val=(start_date,end_date,start_date,end_date,)
		mycursor.execute(event_statement, event_val)
		tuples=mycursor.fetchall()
		for i in tuples:
			events.append(tuple_to_event(i))
	return events
def find_event_by_location(location):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	event_statement="""SELECT event.id,event.name,event.date_start,event.time_start,event.date_end,event.time_end,event.idlocation 
					FROM event e 
					WHERE e.idlocation='%s'""" 
	event_val=(name,)
	mycursor.execute(event_statement, event_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		events.append(tuple_to_event(i))
	return events
def find_event_by_post(post):
	return None
def find_event_by_user(user):
	return None


#finding locations
def find_location_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	locations=[]
	location_statement="""SELECT location.id, location.gps_long, location.gps_lat,location.name, location.radius 
					FROM location l,post p 
					WHERE  p.id='%s' AND l.id=p.idLocation"""
	location_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(location_statement, location_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		locations.append(tuple_to_location(i))
	return locations
def find_location_by_event(event):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	locations=[]
	location_statement="""SELECT location.id, location.gps_long, location.gps_lat,location.name, location.radius 
					FROM location l,event e 
					WHERE  e.id='%s' AND l.id=e.idlocation"""
	location_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(location_statement, location_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		locations.append(tuple_to_location(i))
	return locations
def find_location_by_location(location):
	return None

#finding posts
def find_post_by_event(event):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	
	post_statement="""SELECT post.id,post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,post.idUser,post.idLocation
					FROM event e, post p,postevent pe 
					WHERE  e.id=pe.idevent AND p.id=pe.idPost AND e.id='%s'"""
	post_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(tuple_to_post(i))
	return posts

def find_post_by_user(user):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	post_statement="""SELECT post.id,post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,post.idUser,post.idLocation
					FROM user u,post p 
					WHERE  u.id='%s' AND p.idUser=u.id"""
	post_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(tuple_to_post(i))
	return posts

def find_post_by_location(location):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	post_statement="""SELECT post.id,post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,post.idUser,post.idLocation
					FROM location l,post p 
					WHERE  l.id='%s' AND p.idLocation=l.id"""
	post_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(tuple_to_post(i))
	return posts

def find_post_by_url(url):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	
	post_statement="""SELECT post.id,post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,post.idUser,post.idLocation
					FROM url u, post p,url_post up
					WHERE  u.id=up.idurl AND p.id=up.idPost AND u.id='%s'"""
	post_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(tuple_to_post(i))
	return posts

#finding media
	
def find_media_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	
	post_statement="""SELECT post.id,post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,post.idUser,post.idLocation
					FROM url u, post p,url_post up
					WHERE  u.id=up.idurl AND p.id=up.idPost AND u.id='%s'"""
	post_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(tuple_to_post(i))
	return posts
#find url
def find_url_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	
	post_statement="""SELECT post.id,post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,post.idUser,post.idLocation
					FROM url u, post p,url_post up
					WHERE  u.id=up.idurl AND p.id=up.idPost AND u.id='%s'"""
	post_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(tuple_to_post(i))
	return posts
	
#finding user
def find_user_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	post_statement="""SELECT post.id,post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,post.idUser,post.idLocation
					FROM user u,post p 
					WHERE  u.id='%s' AND p.idUser=u.id"""
	post_val=(start_date,end_date,start_date,end_date,)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(tuple_to_post(i))
	return posts
def find_user_by_event(event):
	#complicated query

#finding tag
def find_tag_by_event(event):

def testing():
