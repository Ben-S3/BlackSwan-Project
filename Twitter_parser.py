# Author: Benjamin Stark
# Date Created: 3/28/2021
# Date updated: 3/29/2021
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
    #return insertEvent(event_insert, event_loc, event_tags)

def parseTweet(tweetArray):
    tweet_user = database_objects.user(None, tweetArray[1], tweetArray[2], tweetArray[3])
    tweet_loc = database_objects.location(None, tweetArray[5], tweetArray[6], tweetArray[7], tweetArray[8])
    tweet_url = database_objects.url(None, tweetArray[10])
    tweet_post = database_objects.post(None, tweetArray[12], tweetArray[13], tweetArray[14], tweetArray[15], tweetArray[16], tweetArray[17], tweetArray[18], tweetArray[19], None, tweetArray[21], tweetArray[22], tweetArray[23], tweetArray[24], None, None)
    tweet_media = database_objects.media(None, tweetArray[28], tweetArray[29], tweetArray[30])
    #insertTweet(tweet_user, tweet_post, tweet_loc, tweet_url, tweet_media)
