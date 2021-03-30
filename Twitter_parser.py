# Author: Benjamin Stark & Bradley Franklin
# Date Created: 3/28/2021
# Date updated: 3/30/2021
# Description: Twitter parser for turning tweets into database objects

import enum
class Tarray(enum.Enum):
    Name = 1
    Website = 2
    Screenname = 3
    Long = 5
    Lat = 6
    Loc = 7
    Rad = 8
    URL = 10
    Title = 12
    Date = 13
    Time = 14
    Desc = 15
    Like = 16
    Comment = 17
    Dislike = 18
    isComment = 19
    PostURL = 21
    Sensitive = 22
    Lang = 23
    Share = 24
    Data = 28
    Media = 29
    Runtime = 30

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
    tweet_user = database_objects.user(None, tweetArray[Tarray.Name.value], tweetArray[Tarray.Website.value], tweetArray[Tarray.Screenname.value])
    tweet_loc = database_objects.location(None, tweetArray[Tarray.Long.value], tweetArray[Tarray.Lat.value], tweetArray[Tarray.Loc.value], tweetArray[Tarray.Rad.value])
    tweet_url = database_objects.url(None, tweetArray[Tarray.URL.value])
    tweet_post = database_objects.post(None, tweetArray[Tarray.Title.value], tweetArray[Tarray.Date.value], tweetArray[Tarray.Time.value], tweetArray[Tarray.Desc.value], tweetArray[Tarray.Like.value], tweetArray[Tarray.Comment.value], tweetArray[Tarray.Dislike.value], tweetArray[Tarray.isComment.value], None, tweetArray[Tarray.PostURL.value], tweetArray[Tarray.Sensitive.value], tweetArray[Tarray.Lang.value], tweetArray[Tarray.Share.value], None, None)
    tweet_media = database_objects.media(None, tweetArray[Tarray.Data.value], tweetArray[Tarray.Media.value], tweetArray[Tarray.Runtime.value])

    insertTweet(tweet_user, tweet_post, tweet_loc, tweet_url, tweet_media)

