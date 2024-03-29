# Author: Hope Church
# Date Created: 3/17/2021
# Date updated: 3/31/2021
# Description: pseudo object-relational mapping of database tables as python objects

import math

class user:
	id_=0
	username=""
	website=""
	displayname=""
	def __init__(self,id_,username,website,displayname):
		self.id_=id_
		self.username=username
		self.website=website
		self.displayname=displayname

class event:
	id_=0
	name=""
	date_start=""
	time_start=""
	date_end=""
	time_end=""
	idlocation=0
	def __init__(self,id_,name,date_start,time_start,date_end,time_end,idlocation):
		self.id_=id_
		self.name=name
		self.date_start=date_start
		self.time_start=time_start
		self.date_end=date_end
		self.time_end=time_end
		self.idlocation=idlocation
	def is_during_event(date,time): #check if date and time is during event
		return None
	def is_during_event(event1): #check if event intersects with this event
		return None

class tag:
	id_=0
	name=""
	def __init__(self,id_, name):
		self.id_=id_
		self.name=name
	
class location:
	id_=0
	gps_long=""
	gps_lat=""
	name=""
	radius=0
	def __init__(self,id_, gps_long, gps_lat,name, radius):
		self.id_=id_
		self.gps_long=gps_long
		self.gps_lat=gps_lat
		self.name=name
		self.radius=radius
	def in_location(longi, lat, rad): #calculate if a gps coordinate and radius intersects with this location
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
	id_=0
	url=""
	def __init__(self,id_, url):
		self.id_=id_
		self.url=url
	def resolve_url(): #resolve true destination of the url
		return None
	def grab_url(): #download contents of url
		return None

class post:
	id_=0
	title=""
	date=""
	time=""
	description=""
	like_num=0
	comment_num=0
	dislike_num=0
	is_comment=False
	parentid=0
	url=""
	issensitive=False
	language=""
	sharecount=0
	idUser=0
	idLocation=0
	def __init__(self,id_,title,date,time,description,like_num,comment_num,dislike_num,is_comment,parentid,url,issensitive,language,sharecount,idUser,idLocation):
		self.id_=id_
		self.title=title
		self.date=date
		self.time=time
		self.description=description
		self.like_num=like_num
		self.comment_num=comment_num
		self.dislike_num=dislike_num
		self.is_comment=is_comment
		self.parentid=parentid
		self.url=url
		self.issensitive=issensitive
		self.language=language
		self.sharecount=sharecount
		self.idUser=idUser
		self.idLocation=idLocation
	def like_ratio(): #ratio of likes to dislikes
		return like_num/dislike_num
	def comment_ratio():#ratio of likes &shares to comments
		return (like_num + sharecount) / comment_num

class media:
	id_=0
	data=""
	media_type=""
	runtime=""
	def __init__(self,id_, data, media_type,runtime):
		self.id_=id_
		self.data=data
		self.media_type=media_type
		self.runtime=runtime
	def is_same(media1): #determine if media is the same as another media #beyond minimal product
		return None
		return None
	def compress(): #compress media to save space, beyond minimal product
		return None

#conversion functions
def tuple_to_event(data):
	return event(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
def tuple_to_user(data):
	return user(data[0],data[1],data[2],data[3])
def tuple_to_post(data):
	return post(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15])
def tuple_to_location(data):
	return location(data[0],data[1],data[2],data[3],data[4])
def tuple_to_tag(data):
	return tag(data[0],data[1])
def tuple_to_url(data):
	return url(data[0],data[1])
def tuple_to_media(data):
	return media(data[0],data[1],data[2],data[3])
