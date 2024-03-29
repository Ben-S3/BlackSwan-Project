#Author: Brian Contreras & Benjamin Stark & Bradley Franklin
#Date: 3/30/2021
#Update: 5/4/2021
#Description: A process to download the media data from a tweet to be sent to the database

import wget
import os
import tweepy
from tweepy import OAuthHandler


auth = OAuthHandler('P3MouxIBM8paKK5WU9nq8rkDQ', '8WFkiLm136rtGfiHc8LQNpiUaQvXHrXDybUFJ55SeijbAvBzjV')
auth.set_access_token('3930122292-nE61z1YrkLLtfWCiDDLQJI6AylW62EJHBpZ8jWt',
'ehRrZd1gvNCgHgrm3jr7wNP0hbn6tJxE8VusJxLH9Iybz')

api = tweepy.API(auth)

#Function to download tweet data if available, then turns data into an array of BLOBS and returns the BLOB array
def downloadMedia(tweetID):
    #Stores tweet
    tweet = getTweetData(tweetID)
    #Checks if the tweet has media files in it
    if tweetHasMedia(tweet) == False:
        print("Tweet does not have media")
        return []

    #If the tweet has media files
    else:
        media = []

        #If the media type is a video
        if mediaType(tweet) == "video":
            filename = wget.download(tweet.extended_entities['media'][0]['video_info']['variants'][0]['url'])
            blobs = turnToBLOB(filename)
            media.append([blobs, "video",  tweet.extended_entities['media'][0]['video_info']['duration_millis']])
            os.remove(filename)
            return media

        #If the media type is a GIF
        elif mediaType(tweet) == "animated_gif":
            filename = wget.download(tweet.extended_entities['media'][0]['media_url'])
            blobs = turnToBLOB(filename)
            media.append([blobs, "animated_gif", 0])
            os.remove(filename)
            return media

        #If the media type is a photo
        elif mediaType(tweet) == "photo":
            for x in range(len(tweet.extended_entities['media'])):
                filename = wget.download(tweet.extended_entities['media'][x]['media_url'])
                blobs = turnToBLOB(filename)
                media.append([blobs, "photo",  0])
                os.remove(filename)
            return media


#Function to obtain the tweet itself from the tweet data
def getTweetData(tweetID):
    try:
        tweet = api.get_status(tweetID, tweet_mode="extended")
        return tweet
    except:
        print("An error occurred accessing this tweet's media.")
        return None

#Function to check if the tweet has media files in it
def tweetHasMedia(tweet):
    if len(tweet.entities.get('media', [])) > 0:
        return True
    else:
        return False

#Function to check the type of media the tweet has
def mediaType(tweet):
    if tweet.extended_entities['media'][0]['type'] == "photo":
        return "photo"
    elif tweet.extended_entities['media'][0]['type'] == "video":
        return "video"
    else:
        return "animated_gif"

#Function to turn media data into a BLOB object
def turnToBLOB(filename):
    with open(filename, 'rb') as file:
        blob = file.read()
    return blob
