# Author: Hope Church
# Date Created: 3/17/2021
# Date updated: 3/31/2021
# Description: pseudo object-relational mapping of database tables as python objects

import math

class user:
	id_
	username
	website
	displayname
	def __init__(self,idUser,username,website,displayname):
		self.idUser=idUser
		self.username=username
		self.website=website
		self.displayname=displayname

class event:
	id_
	name
	date_start
	time_start
	date_end
	time_end
	idlocation
	def __init__(self,id_,name,date_start,time_start,date_end,time_end,idlocation):
		self.id_=id_
		self.name=name
		self.date_start=date_start
		self.time_start=time_start
		self.date_end=date_end
		self.time_end=time_end
		self.idlocation=idlocation
	def is_during_event(date,time): #check if date and time is during event
		#TODO
	def is_during_event(event1): #check if event intersects with this event
		#TODO

class tag:
	id_
	name
	def __init__(self,id_, name):
		self.id_=id_
		self.name=name
	
class location:
	id_
	gps_long
	gps_lat
	name
	radius
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
	id_
	url
	def __init__(self,id_, url):
		self.id_=id_
		self.url=url
	def resolve_url(): #resolve true destination of the url
		#TODO
	def grab_url(): #download contents of url
		#TODO

class post:
	id_
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
	idLocation
	def __init__(self,id_,title,date,time,description,like_num,comment_num,dislike_num,is_comment,parentid,url,issensitive,language,sharecount,idUser):
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
	id_
	data
	media_type
	runtime
	def __init__(id_, data, media_type,runtime):
		self.id_=id_
		self.data=data
		self.media_type=media_type
		self.runtime=runtime
	def is_same(media1): #determine if media is the same as another media #beyond minimal product
		#TODO
		return None
	def compress(): #compress media to save space, beyond minimal product
		#TODO
