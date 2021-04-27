# Author: Hope Church
# Date Created: 3/27/2021
# Date updated: 4/5/2021
# Description: inserts objects into database given by parser
import database_objects as dbo #not how you import files, here for reference
import mysql.connector



#insert example
#statement="INSERT INTO user (username,website,displayname) VALUES ( %s,%s, %s)"
#val=(user.username,user.website,user.displayname)
#mycursor.execute(statement, val)

#how to get the primary key of the previous transaction:
#mycursor.lastrowid

#checks if event exists and returns a list of ids found
def event_exists(event):
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	events=[]
	print("checking if event exists")
	test_statement="SELECT id FROM event WHERE name LIKE %s"
	test_val=('%'+event.name+'%',)
	mycursor.execute(test_statement, test_val)
	tuples=mycursor.fetchall()
	for i in tuples:
		events.append(dbo.tuple_to_event(i))
	return events

def stage_one(location,event,tags): #inserts location, event, and array of tags, and returns a tuple [idlocation,idevent] order is location > event > tags
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	
	#insert location
	print("inserting location",location.name)
	location_statement="INSERT INTO location (gps_long,gps_lat,name, radius) VALUES ( %s,%s, %s,%s)"
	location_val=(location.gps_long,location.gps_lat,location.name, location.radius)
	mycursor.execute(location_statement, location_val)
	#get idlocation
	location.id_=mycursor.lastrowid
	print("inserted location with id",location.id_)
	
	#insert event if id is not already given to account for potentially existing events
	if event.id_ is None:
		print("inserting event",event.name)
		event_statement="INSERT INTO event (name,date_start,time_start,date_end,time_end,idlocation) VALUES ( %s,%s, %s,%s,%s,%s)"
		event_val=(event.name,event.date_start,event.time_start,event.date_end,event.time_end,location.id_)
		mycursor.execute(event_statement, event_val)
		#get idevent
		event.id_=mycursor.lastrowid
		print("inserted event with id",event.id_)
	else:
		print("event id",event.id_,"already given")

	#insert tag array
	print("inserting tags")
	for temp in range(len(tags)):
		cur=tags[temp]
		tag_statement="INSERT INTO tag (name) VALUES (%s)"
		tag_val=(cur.name,)
		#try to insert tag
		try:
			print("inserting tag",cur.name)
			mycursor.execute(tag_statement, tag_val)
			#set tag id
			tags[temp].id_=mycursor.lastrowid
			print("inserted tag with id",tags[temp].id_)
		#if tag already exists
		except mysql.connector.errors.IntegrityError:
			
			#get id from the existing tag
			err_statement="SELECT id FROM tag WHERE name=%s"
			err_val=(cur.name,)
			mycursor.execute(err_statement, err_val)
			tags[temp].id_ = int(mycursor.fetchone()[0])
			print("tag", cur.name, "already exists, using existing id",tags[temp].id_)
		print("associating tag",tags[temp].id_, "and event",event.id_)
		#associate tag and event
		tagevent_statement="INSERT INTO tagevent (idtag,idevent) VALUES ( %s,%s)"
		tagevent_val=(tags[temp].id_ , event.id_)
		mycursor.execute(tagevent_statement, tagevent_val)
	
	#commit to database
	mydb.commit()
	return [location.id_, event.id_]

def stage_two(idevent, medias, urls, user, post,location): #inserts media array, url array, user, location, and post. order is location > user > post > url > media, returns nothing
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	
	#insert location as long as it has some attribute whatsoever
	
	if location.gps_lat is not None or location.gps_long is not None or location.name is not None:
		print("inserting location",location.name)
		location_statement="INSERT INTO location (gps_long,gps_lat,name, radius) VALUES ( %s,%s, %s,%s)"
		location_val=(location.gps_long,location.gps_lat,location.name, location.radius)
		mycursor.execute(location_statement, location_val)
		#get idlocation
		location.id_=mycursor.lastrowid
		print("inserted location with id",location.id_)
	else:
		print("location has no information, not inserting")
	
	#test if user exists
	user_test="SELECT * FROM user WHERE username=%s AND website=%s"
	user_test_val=(user.username,user.website)
	mycursor.execute(user_test, user_test_val)
	result=mycursor.fetchone()
	#if user doesn't exist
	if not result:
		print("inserting user",user.username, "at website",user.website)
		#insert user
		user_statement="INSERT INTO user (username,website,displayname) VALUES ( %s,%s, %s)"
		user_val=(user.username,user.website,user.displayname)
		mycursor.execute(user_statement, user_val)
		#get userid
		user.id_=mycursor.lastrowid
		print("inserted user with id",user.id_)
	else:
		#set user to existing user
		user.id_=int(result[0])
		print("existing user" ,user.username,"at website", user.website, "using existing user id",user.id_)
	
	#insert post
	print("inserting post")
	post_statement="INSERT INTO post (title,date,time,description,like_num,comment_num,dislike_num,is_comment,parentid,url,issensitive,language,sharecount,idUser,idLocation) VALUES ( %s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	post_val=(post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,user.id_,location.id_)
	mycursor.execute(post_statement, post_val)
	#get idpost
	post.id_=mycursor.lastrowid
	print("inserted post with id",post.id_)
	
	#insert url array
	print("inserting urls")
	for temp in range(len(urls)):
		cur=urls[temp]
		#insert a url
		url_statement="INSERT INTO url (url) VALUES ( %s)"
		url_val=(cur.url,)
		#only insert non-null url
		if cur.url is not None:
			print("inserting url",cur.url)
			#try to insert url
			try:
				mycursor.execute(url_statement, url_val)
				#set url id
				urls[temp].id_=mycursor.lastrowid
				print("inserted url with id",urls[temp].id_)
			#if url already exists
			except mysql.connector.errors.IntegrityError:
				
				err_statement="SELECT id FROM url WHERE url=%s"
				err_val=(cur.url,)
				mycursor.execute(err_statement, err_val)
				#set url id to existing url id
				urls[temp].id_ = int(mycursor.fetchone()[0])
				print("url", cur.url,"already exists, using existing id",urls[temp].id_)
			print("associating url",urls[temp].id_," and post",post.id_)
			#associate post and url
			url_post_statement="INSERT INTO url_post (idPost,idurl) VALUES ( %s,%s)"
			url_post_val=(post.id_,urls[temp].id_)
			mycursor.execute(url_post_statement, url_post_val)
		else:
			print("url is null, not inserting")
	
	print("inserting media")
	#insert media array
	for temp in range(len(medias)):
		cur=medias[temp]
		media_statement="INSERT INTO media (data, media_type,runtime) VALUES (%s,%s,%s)"
		#media has to exist
		if cur.data is not None:
			#insert media
			media_val=(cur.data, cur.media_type,cur.runtime)
			mycursor.execute(media_statement, media_val)
			#set media id
			medias[temp].id_=mycursor.lastrowid
			print("associating media",medias[temp].id_, "and post",post.id_)
			#associate media and post
			media_post_statement="INSERT INTO media_post (idpost, idmedia) VALUES ( %s,%s)"
			media_post_val=(post.id_,medias[temp].id_)
			mycursor.execute(media_post_statement, media_post_val)
		else:
			print("media is null, not inserting")

		
	print("associating post",post.id_," and event",idevent)
	#insert postevent
	postevent_statement="INSERT INTO postevent (idPost,idevent) VALUES ( %s,%s)"
	postevent_val=(post.id_,idevent)
	mycursor.execute(postevent_statement, postevent_val)
		

	
	mydb.commit()
	
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

#testing zone
def testing():
	testevent=dbo.event(None, "testevent", "2020-10-10", "11:00:00","2020-10-10", "11:00:00",None)
	testlocation=dbo.location(None, "0.0","0.0","testlocation","100")
	testuser=dbo.user(None,"testuser","twitter.com","displayname") 
	testpost=dbo.post(None,"title","2020-10-10","11:00:00","description",15,15,15,False,None,"twitter.com",False,"en",17,None,None)
	testmedia=dbo.media(None, "testdata","png","00:00")
	testtag=dbo.tag(None,"testtag")
	testurl=dbo.url(None,"twitter.com")
	temp=stage_one(testlocation,testevent,[testtag])
	idevent=temp[1]
	stage_two(idevent,[testmedia], [testurl],testuser,testpost,testlocation)
