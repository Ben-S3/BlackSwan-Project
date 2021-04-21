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

#-------------------------------------finding events--------------------------------------------#
def find_events_by_name(name):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	event_statement="""SELECT id,name,date_start,time_start,date_end,time_end,idlocation 
                    FROM event 
                    WHERE name LIKE %s"""
	event_val=('%'+name+'%',)
	print("selecting events by name:",name)
	mycursor.execute(event_statement, event_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		events.append(dbo.tuple_to_event(i))
	return events


def find_events_by_date(start_date,end_date):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	event_statement="""SELECT id,name,date_start,time_start,date_end,time_end,idlocation 
					FROM event 
					WHERE  date_start BETWEEN  %s %s OR date_end BETWEEN %s,%s"""
	event_val=(start_date,end_date,start_date,end_date,)
	print("selecting events by date",start_date,end_date)
	mycursor.execute(event_statement, event_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		events.append(dbo.tuple_to_event(i))
	return events

def find_event_by_keywords(keywords):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	print("selecting events by keywords")
	for i in keywords:
		event_statement="""SELECT e.id,e.name,e.date_start,e.time_start,e.date_end,e.time_end,e.idlocation 
						FROM event e,tag t,tagevent te 
						WHERE  e.id=te.idevent AND t.id=te.idtag AND t.name LIKE %s"""
		event_val=('%'+i+'%',)
		print("selecting events by keyword:",i)
		mycursor.execute(event_statement, event_val)
		tuples=mycursor.fetchall()
		for i in tuples:
			events.append(dbo.tuple_to_event(i))
	return events

def find_event_by_keywords_in_posts(keywords):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	print("selecting events by keywords in posts")
	for i in keywords:
		event_statement="""SELECT e.id,e.name,e.date_start,e.time_start,e.date_end,e.time_end,e.idlocation 
						FROM event e, postevent pe, post p
						WHERE  e.id=pe.idevent AND p.id=pe.idPost AND (post.title LIKE %s OR post.description LIKE %s)"""
		event_val=('%'+i+'%','%'+i+'%')
		print("selecting events by keyword in posts:",i)
		mycursor.execute(event_statement, event_val)
		tuples=mycursor.fetchall()
		for i in tuples:
			events.append(dbo.tuple_to_event(i))
	return events

def find_event_by_location(location):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	event_statement="""SELECT e.id,e.name,e.date_start,e.time_start,e.date_end,e.time_end,e.idlocation 
					FROM event e 
					WHERE e.idlocation=%s""" 
	event_val=(location.id_,)
	print("selecting events by location:",location.id_)
	mycursor.execute(event_statement, event_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		events.append(dbo.tuple_to_event(i))
	return events

def find_event_by_post(post):
	return None

def find_event_by_user(user):
	return None


#---------------finding locations-----------------------#
def find_location_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	locations=[]
	location_statement="""SELECT l.id, l.gps_long, l.gps_lat,l.name, l.radius 
					FROM location l,post p 
					WHERE  p.id=%s AND l.id=p.idLocation"""
	location_val=(post.id_,)
	print("selecting location by post:",post.id_)
	mycursor.execute(location_statement, location_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		locations.append(dbo.tuple_to_location(i))
	return locations

def find_location_by_event(event):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	locations=[]
	location_statement="""SELECT l.id, l.gps_long, l.gps_lat,l.name, l.radius 
					FROM location l,event e 
					WHERE  e.id=%s AND l.id=e.idlocation"""
	location_val=(event.id_,)
	print("selecting location by event:",event.id_)
	mycursor.execute(location_statement, location_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		locations.append(dbo.tuple_to_location(i))
	return locations

def find_location_by_location(location): #find locations that intersect with a location, use rectangle instead of radius?
	return None

#----------------------finding posts-----------------------#
def find_post_by_event(event):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	
	post_statement="""SELECT p.id,p.title,p.date,p.time,p.description,p.like_num,p.comment_num,p.dislike_num,p.is_comment,p.parentid,p.url,p.issensitive,p.language,p.sharecount,p.idUser,p.idLocation
					FROM event e, post p,postevent pe 
					WHERE  e.id=pe.idevent AND p.id=pe.idPost AND e.id=%s"""
	post_val=(event.id_,)
	print("selecting posts by event:",event.id_)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(dbo.tuple_to_post(i))
	return posts

def find_post_by_user(user):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	post_statement="""SELECT p.id,p.title,p.date,p.time,p.description,p.like_num,p.comment_num,p.dislike_num,p.is_comment,p.parentid,p.url,p.issensitive,p.language,p.sharecount,p.idUser,p.idLocation
					FROM user u,post p 
					WHERE  u.id=%s AND p.idUser=u.id"""
	post_val=(user.id_,)
	print("selecting posts by user:",user.id_)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(dbo.tuple_to_post(i))
	return posts

def find_post_by_location(location): #TODO: add radius search
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	post_statement="""SELECT p.id,p.title,p.date,p.time,p.description,p.like_num,p.comment_num,p.dislike_num,p.is_comment,p.parentid,p.url,p.issensitive,p.language,p.sharecount,p.idUser,p.idLocation
					FROM post p 
					WHERE  p.idLocation=%s"""
	post_val=(location.id_,)
	print("selecting posts by location:",location.id_)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(dbo.tuple_to_post(i))
	return posts

def find_post_by_url(url):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	posts=[]
	
	post_statement="""SELECT p.id,p.title,p.date,p.time,p.description,p.like_num,p.comment_num,p.dislike_num,p.is_comment,p.parentid,p.url,p.issensitive,p.language,p.sharecount,p.idUser,p.idLocation
					FROM url u, post p,url_post up
					WHERE  u.id=up.idurl AND p.id=up.idPost AND u.id=%s"""
	post_val=(url.id_,)
	print("selecting posts by url:",url.id_)
	mycursor.execute(post_statement, post_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		posts.append(dbo.tuple_to_post(i))
	return posts

#--------------------------------------finding media---------------------------------#
	
def find_media_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	medias=[]
	media_statement="""SELECT m.id, m.data, m.media_type,m.runtime
					FROM media m, post p,media_post mp
					WHERE  m.id=mp.idmedia AND p.id=mp.idpost AND p.id=%s"""
	media_val=(post.id_,)
	print("selecting medias by post:",post.id_)
	mycursor.execute(media_statement, media_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		medias.append(dbo.tuple_to_media(i))
	return medias

#-----------------------------------------------------find url--------------------------------------------------#
def find_url_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	urls=[]
	
	url_statement="""SELECT u.id, u.url
					FROM url u, post p,url_post up
					WHERE  u.id=up.idurl AND p.id=up.idPost AND p.id=%s"""
	url_val=(post.id_,)
	print("selecting urls by post:",post.id_)
	mycursor.execute(url_statement, url_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		urls.append(dbo.tuple_to_url(i))
	return urls
	
#----------------------------------finding user-----------------------------#
def find_user_by_post(post):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	users=[]
	user_statement="""SELECT u.id,u.username,u.website,u.displayname
					FROM user u,post p 
					WHERE  p.id=%s AND p.idUser=u.id"""
	user_val=(post.id_,)
	print("selecting user by post:",post.id_)
	mycursor.execute(user_statement, user_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		users.append(dbo.tuple_to_user(i))
	return users


#------------------------------------finding tag-----------------------------#
def find_tag_by_event(event):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	tags=[]
	tag_statement="""SELECT event.id,event.name,event.date_start,event.time_start,event.date_end,event.time_end,event.idlocation 
					FROM event e,tag t,tagevent te 
					WHERE  e.id=%s AND t.id=te.idtag AND e.id=te.idevent"""
	tag_val=(event.id_,)
	print("selecting tag by event:",event.id_)
	mycursor.execute(tag_statement, tag_val)
	tuples=mycursor.fetchall()
	for i in tuples:
			tags.append(dbo.tuple_to_tag(i))
	return tags

def testing(): #minimally viable product test, run scraper first!
	name_events=find_events_by_name("Minnesota")
	keyword_events=find_event_by_keywords(["Minnesota"])
	posts=find_post_by_event(name_events[0])
	user=find_user_by_post(posts[0])
	medias=find_media_by_post(posts[0])
	urls=find_url_by_post(posts[0])
	print("outputing events found by name")
	for i in name_events:
		print(i.__dict__)
	print("outputing events found by keywords")
	for i in keyword_events:
		print(i.__dict__)
	print("outputing posts")
	for i in posts:
		print(i.__dict__)
	print("outputing user")
	for i in user:
		print(i.__dict__)
	print("outputing media")
	for i in medias:
		print(i.__dict__)
	print("outputting urls")
	for i in urls:
		print(i.__dict__)
testing()
