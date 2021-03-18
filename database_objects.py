# Author: Hope Church
# Date Created: 3/17/2021
# Description: pseudo object-relational mapping of database tables as python objects

import math

class user:
	idUser
	username
	website
	displayname
	follower_count
	follow_count
	def __init__(self,idUser,username,website,displayname,follower_count,follow_count):
		self.idUser=idUser
		self.username=username
		self.website=website
		self.displayname=displayname
		self.follower_count=follower_count
		self.follow_count=follow_count
	def follow_ratio(): #ratio of followers to following
		return follower_count/follow_count

class event:
	idevent
	name
	date_start
	time_start
	date_end
	time_end
	def __init__(self,idevent,name,date_start,time_start,date_end,time_end):
		self.idevent=idevent
		self.name=name
		self.date_start=date_start
		self.time_start=time_start
		self.date_end=date_end
		self.time_end=time_end
	def is_during_event(date,time): #check if date and time is during event
		#TODO
	def is_during_event(event1): #check if event intersects with this event
		#TODO

class tag:
	idtag
	name
	def __init__(self,idtag, name):
		self.idtag=idtag
		self.name=name
	
class location:
	idLocation
	gps_long
	gps_lat
	name
	radius
	def __init__(self,idLocation, gps_long, gps_lat,name, radius):
		#TODO
	def in_location(longi, lat, rad):#calculate if a gps coordinate and radius intersects with this location
		distance=math.sqrt(math.pow(longi-gps_long,2) + math.pow(lat-gps_lat,2))
		if distance < radius + rad:
			return True
		else:
			return False
	def in_location(loc): #calculate if a location intersects with this location
		distance=math.sqrt(math.pow(loc.gps_long-gps_long,2) + math.pow(loc.gps_lat-gps_lat,2))
		if distance < radius + rad:
			return True
		else:
			return False
		

class url:
	idurl
	url
	def __init__(self,idurl, url):
		self.idurl=idurl
		self.url=url
	def resolve_url(): #resolve true destination of the url
		#TODO
	def grab_url(): #download contents of url
		#TODO

class post:
	idPost
	title
	date
	time
	description
	like_num
	comment_num
	dislike_num
	is_comment
	parentid
	url
	issensitive
	language
	sharecount
	idUser
	def __init__(self,idPost,title,date,time,description,like_num,comment_num,dislike_num,is_comment,parentid,url,issensitive,language,sharecount,idUser):
		#TODO
	def like_ratio(): #ratio of likes to dislikes
		return like_num/dislike_num
	def comment_ratio():#ratio of likes &shares to comments
		return (like_num + sharecount) / comment_num

class media:
	idmedia
	data
	media_type
	runtime
	def __init__():
		#TODO
	def is_same(media1): #determine if media is the same as another media #beyond minimal product
		#TODO
		return None
	def compress(): #compress media to save space, beyond minimal product
		#TODO
