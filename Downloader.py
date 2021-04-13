#Author: Brian Contreras & BS & Bradley Franklin
#Date: 3/30/2021
#Update: 3/31/2021
#Description: A class to download the media data from a tweet

import wget
import urllib.request
import tweepy
from tweepy import OAuthHandler


auth = OAuthHandler('P3MouxIBM8paKK5WU9nq8rkDQ', '8WFkiLm136rtGfiHc8LQNpiUaQvXHrXDybUFJ55SeijbAvBzjV')
auth.set_access_token('3930122292-nE61z1YrkLLtfWCiDDLQJI6AylW62EJHBpZ8jWt',
'ehRrZd1gvNCgHgrm3jr7wNP0hbn6tJxE8VusJxLH9Iybz')

api = tweepy.API(auth)


def downloadMedia(tweetID):
    tweet = getTweetData(tweetID)
    if tweetHasMedia(tweet) == False:
        print("Tweet does not have media")
        return []

    else:
        blobs = []
        if mediaType(tweet) == "video":
            filename = wget.download(tweet.extended_entities['media'][0]['media_url'])
            urllib.request.urlretrieve(tweet.extended_entities['media'][0]['media_url'], filename)
            blobs.append(turnToBLOB(filename))
            return blobs

        elif mediaType(tweet) == "animated_gif":
            wget.download(tweet.extended_entities['media'][0]['media_url'])

        elif mediaType(tweet) == "photo":
            for x in range(len(tweet.extended_entities['media'])):
                filename = wget.download(tweet.extended_entities['media'][x]['media_url'])
                blobs.append(turnToBLOB(filename))
            return blobs


def getTweetData(tweetID):
    tweet = api.get_status(tweetID, tweet_mode="extended")
    return tweet

def tweetHasMedia(tweet):
    if len(tweet.entities.get('media', [])) > 0:
        return True
    else:
        return False

def mediaType(tweet):
    if tweet.extended_entities['media'][0]['type'] == "photo":
        return "photo"
    elif tweet.extended_entities['media'][0]['type'] == "video":
        return "video"
    else:
        return "animated_gif"

def turnToBLOB(filename):
    with open(filename, 'rb') as file:
        blob = file.read()
    return blob

