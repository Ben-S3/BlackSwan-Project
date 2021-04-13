#Author: Brian Contreras & BS & Bradley Franklin
#Date: 3/30/2021
#Update: 4/13/2021
#Description: A file to download the media data from a tweet

import wget
import urllib.request
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
        return 0

    #If the tweet has media files
    else:
        blobs = []

        #If the media type if a video
        if mediaType(tweet) == "video":
            filename = wget.download(tweet.extended_entities['media'][0]['media_url'])
            urllib.request.urlretrieve(tweet.extended_entities['media'][0]['media_url'], filename)
            blobs.append(turnToBLOB(filename))
            return blobs

        #If the media type is a gif
        elif mediaType(tweet) == "animated_gif":
            wget.download(tweet.extended_entities['media'][0]['media_url'])

        #If the media type is a photo
        elif mediaType(tweet) == "photo":
            for x in range(len(tweet.extended_entities['media'])):
                filename = wget.download(tweet.extended_entities['media'][x]['media_url'])
                blobs.append(turnToBLOB(filename))
            return blobs


#Function to obtain the tweet itself from the tweet data
def getTweetData(tweetID):
    tweet = api.get_status(tweetID, tweet_mode="extended")
    return tweet

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

