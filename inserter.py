# Author: Hope Church
# Date Created: 3/27/2021
# Date updated: 3/31/2021
# Description: inserts objects into database given by parser
import database_objects as dbo #not how you import files, here for reference
import mysql.connector



#insert example
#statement="INSERT INTO user (username,website,displayname) VALUES ( %s,%s, %s)"
#val=(user.username,user.website,user.displayname)
#mycursor.execute(statement, val)

#how to get the primary key of the previous transaction:
#mycursor.lastrowid

def stage_one(location,event,tags): #inserts location, event, and array of tags, and returns a tuple [idlocation,idevent] order is location > event > tags
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	#insert location
	location_statement="INSERT INTO location (gps_long,gps_lat,name, radius) VALUES ( %s,%s, %s,%s)"
	location_val=(location.gps_long,location.gps_lat,location.name, location.radius)
	mycursor.execute(location_statement, location_val)
	#get idlocation
	location.id_=mycursor.lastrowid
	
	#insert event
	event_statement="INSERT INTO event (name,date_start,time_start,date_end,time_end,idlocation) VALUES ( %s,%s, %s,%s,%s,%s)"
	event_val=(event.name,event.date_start,event.time_start,event.date_end,event.time_end,location.id_)
	mycursor.execute(event_statement, event_val)
	#get idevent
	event.id_=mycursor.lastrowid

	#insert tag array
	for temp in range(len(tags)):
		cur=tags[temp]
		#insert a tag
		tag_statement="INSERT INTO tag (name) VALUES (%s)"
		tag_val=(cur.name,)
		try:
			mycursor.execute(tag_statement, tag_val)
			#set tag id
			tags[temp].id_=mycursor.lastrowid
		except mysql.connector.errors.IntegrityError:
			err_statement="SELECT id FROM tag WHERE name=%s"
			err_val=(cur.name,)
			mycursor.execute(err_statement, err_val)
			tags[temp].id_ = int(mycursor.fetchone()[0])
		tagevent_statement="INSERT INTO tagevent (idtag,idevent) VALUES ( %s,%s)"
		tagevent_val=(tags[temp].id_ , event.id_)
		mycursor.execute(tagevent_statement, tagevent_val)
		
	

	mydb.commit()
	return [location.id_, event.id_]

def stage_two(idevent, medias, urls, user, post,location): #inserts media array, url array, user, location, and post. order is location > user > post > url > media, returns nothing
	temp=db_connect()
	mydb=temp[0]
	mycursor=temp[1]
	
	#insert location
	if location.gps_lat is not None or location.gps_long is not None or location.name is not None:
		location_statement="INSERT INTO location (gps_long,gps_lat,name, radius) VALUES ( %s,%s, %s,%s)"
		location_val=(location.gps_long,location.gps_lat,location.name, location.radius)
		mycursor.execute(location_statement, location_val)
		#get idlocation
		location.id_=mycursor.lastrowid
	
	#test if user exists
	user_test="SELECT * FROM user WHERE username=%s AND website=%s"
	user_test_val=(user.username,user.website)
	mycursor.execute(user_test, user_test_val)
	result=mycursor.fetchone()
	if not result:
		#insert user
		user_statement="INSERT INTO user (username,website,displayname) VALUES ( %s,%s, %s)"
		user_val=(user.username,user.website,user.displayname)
		mycursor.execute(user_statement, user_val)
		#get userid
		user.id_=mycursor.lastrowid
	else:
		user.id_=int(result[0])
	
	#insert post
	post_statement="INSERT INTO post (title,date,time,description,like_num,comment_num,dislike_num,is_comment,parentid,url,issensitive,language,sharecount,idUser,idLocation) VALUES ( %s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	post_val=(post.title,post.date,post.time,post.description,post.like_num,post.comment_num,post.dislike_num,post.is_comment,post.parentid,post.url,post.issensitive,post.language,post.sharecount,user.id_,location.id_)
	mycursor.execute(post_statement, post_val)
	#get idpost
	post.id_=mycursor.lastrowid
	
	#insert url array
	for temp in range(len(urls)):
		cur=urls[temp]
		#insert a url
		url_statement="INSERT INTO url (url) VALUES ( %s)"
		url_val=(cur.url,)
		if cur.url is not None:
			try:
				mycursor.execute(url_statement, url_val)
				#set url id
				urls[temp].id_=mycursor.lastrowid
			except mysql.connector.errors.IntegrityError:
				err_statement="SELECT id FROM url WHERE url=%s"
				err_val=(cur.url,)
				mycursor.execute(err_statement, err_val)
				urls[temp].id_ = int(mycursor.fetchone()[0])
			url_post_statement="INSERT INTO url_post (idPost,idurl) VALUES ( %s,%s)"
			url_post_val=(post.id_,urls[temp].id_)
			mycursor.execute(url_post_statement, url_post_val)
	
	#insert media array
	for temp in range(len(medias)):
		cur=medias[temp]
		#insert a tag
		media_statement="INSERT INTO media (data, media_type,runtime) VALUES (%s,%s,%s)"
		if cur.data is not None:
			media_val=(cur.data, cur.media_type,cur.runtime)
			mycursor.execute(media_statement, media_val)
			#set tag id
			medias[temp].id_=mycursor.lastrowid
			#insert media_post
			media_post_statement="INSERT INTO media_post (idpost, idmedia) VALUES ( %s,%s)"
			media_post_val=(post.id_,medias[temp].id_)
			mycursor.execute(media_post_statement, media_post_val)

		
		
	#insert postevent
	postevent_statement="INSERT INTO postevent (idPost,idevent) VALUES ( %s,%s)"
	postevent_val=(post.id_,idevent)
	mycursor.execute(postevent_statement, postevent_val)
		

	
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
