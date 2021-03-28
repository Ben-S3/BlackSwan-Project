# Author: Benjamin Stark
# Date Created: 3/28/2021
# Date updated: 3/28/2021
# Description: Twitter parser for turning tweets into database objects

import database_objects

def parseSearchData(eventName, dataStart, timeStart, dateEnd, timeEnd, latitude, longitude, loc_name, rad, tags):
    event_insert = database_objects.event(None, eventName, dataStart, timeStart, dateEnd, timeEnd, None)
    event_loc = database_objects.location(None, longitude, latitude, loc_name, rad)
    event_tags = [0] * len(tags)
    i = 0
    for x in tags:
        event_tags[i] = database_objects.tag(None, x)
        i = i + 1
    return insertEvent(event_insert, event_loc, event_tags)

def parseTweet(tweetArray):
    tweet_user = database_objects.user(None, username, website, displayname)
    tweet_loc = database_objects.location(None, gps_long, gps_lat, name, radius)
    tweet_url = database_objects.url(None, url)
    tweet_post = database_objects.post(None, title, date, time, description, like_num, comment_num, dislike_num, is_comment, None, url, issensitive, language, sharecount, None)
    tweet_media = database_objects.media(None, data, media_type, runtime)
    insertTweet(tweet_user, tweet_post, tweet_loc, tweet_url, tweet_media)

