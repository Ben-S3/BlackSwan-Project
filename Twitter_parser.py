# Author: Benjamin Stark
# Date Created: 3/28/2021
# Date updated: 3/28/2021
# Description: Twitter parser for turning tweets into database objects

import database_objects

def parseSearchData(eventName, dataStart, timeStart, dateEnd, timeEnd, latitude, longitude, loc_name, rad, tags):
    event_insert = database_objects.event(101010101, eventName, dataStart, timeStart, dateEnd, timeEnd, 111111)
    event_loc = database_objects.location(111111, longitude, latitude, loc_name, rad)
    event_tags = [0] * len(tags)
    i = 0
    for x in tags:
        event_tags[i] = database_objects.tag(100+i, x)
        i = i + 1
    return insertEvent(event_insert, event_loc, event_tags)

def parseTweet(tweetArray):
    tweet_user = database_objects.user(idUser, username, website, displayname)
    tweet_loc = database_objects.location(idLocation, gps_long, gps_lat, name, radius)
    tweet_url = database_objects.url(idurl, url)
    tweet_post = database_objects.post(idPost, title, date, time, description, like_num, comment_num, dislike_num, is_comment, parentid, url, issensitive, language, sharecount, idUser)
    tweet_media = database_objects.media(idmedia, data, media_type, runtime)
    insertTweet(tweet_user, tweet_post, tweet_loc, tweet_url, tweet_media)

