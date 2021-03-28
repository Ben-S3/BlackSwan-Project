# Author: Hope Church, BS
# Date Created: 3/17/2021
# Date updated: 3/28/2021
# Description: pseudo object-relational mapping of database tables as python objects

import math


class user:
    def __init__(self, idUser, username, website, displayname):
        self.idUser = idUser
        self.username = username
        self.website = website
        self.displayname = displayname


class event:
    def __init__(self, idevent, name, date_start, time_start, date_end, time_end, idLocation):
        self.idevent = idevent
        self.name = name
        self.date_start = date_start
        self.time_start = time_start
        self.date_end = date_end
        self.time_end = time_end
        self.idLocation = idLocation

   # def is_during_event(date, time):  # check if date and time is during event
        # TODO

   # def is_during_event(event1):  # check if event intersects with this event
        # TODO


class tag:
    def __init__(self, idtag, name):
        self.idtag = idtag
        self.name = name


class location:
    def __init__(self, idLocation, gps_long, gps_lat, name, radius):
        self.idLocation = idLocation
        self.gps_long = gps_long
        self.gps_lat = gps_lat
        self.name = name
        self.radius = radius

    def in_location(self, longi, lat, rad):  # calculate if a gps coordinate and radius intersects with this location
        distance = math.sqrt(math.pow(longi - self.gps_long, 2) + math.pow(lat - self.gps_lat, 2))
        if distance < self.radius + rad:
            return True
        else:
            return False

    def in_location(self, loc):  # calculate if a location intersects with this location
        distance = math.sqrt(math.pow(loc.gps_long - self.gps_long, 2) + math.pow(loc.gps_lat - self.gps_lat, 2))
        if distance < self.radius + self.rad:
            return True
        else:
            return False


class url:
    def __init__(self, idurl, url):
        self.idurl = idurl
        self.url = url

    #def resolve_url():  # resolve true destination of the url

    # TODO
    #def grab_url():  # download contents of url


# TODO

class post:
    def __init__(self, idPost, title, date, time, description, like_num, comment_num, dislike_num, is_comment, parentid,
                 url, issensitive, language, sharecount, idUser, idLocation):
        self.idPost = idPost
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.like_num = like_num
        self.comment_num = comment_num
        self.dislike_num = dislike_num
        self.is_comment = is_comment
        self.parentid = parentid
        self.url = url
        self.issensitive = issensitive
        self.language = language
        self.sharecount = sharecount
        self.idUser = idUser
        self.idLocation = idLocation

    def like_ratio(self):  # ratio of likes to dislikes
        return self.like_num / self.dislike_num

    def comment_ratio(self):  # ratio of likes &shares to comments
        return (self.like_num + self.sharecount) / self.comment_num


class media:
    def __init__(self, idmedia, data, media_type, runtime):
        self.idmedia = idmedia
        self.data = data
        self.media_type = media_type
        self.runtime = runtime

    def is_same(media1):  # determine if media is the same as another media #beyond minimal product
        # TODO
        return None

    #def compress():  # compress media to save space, beyond minimal product
# TODO
