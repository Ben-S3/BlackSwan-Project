# Author: Bradley Franklin & Hope Church
# Date Created: 2/9/2021
# Date updated: 5/4/2021
# Description:  Basic Scraper of Twitter to find tweets and break data to be sent to parser
#               Includes tweepy to access Twitter API, geopy to access geolocation of tweets

import sys
import time
import csv
import datetime
import tweepy
from tweepy import OAuthHandler
import geopy
from geopy.geocoders import Nominatim

import Twitter_parser

def Scrape(eventName, keywords, latitude, longitude, radius, start_date, start_time, end_date, end_time, event_id):
    # Test whether fields were filled out, if not, exit
    if (eventName == "Event Name" or keywords == "Keywords" or longitude == "Longitude" or latitude == "Latitude" or
            radius == "Radius" or start_date == "Start Date" or end_date == "End Date"):
        print("Please fill out all fields.")
        exit()

    auth = OAuthHandler('P3MouxIBM8paKK5WU9nq8rkDQ', '8WFkiLm136rtGfiHc8LQNpiUaQvXHrXDybUFJ55SeijbAvBzjV')
    auth.set_access_token('3930122292-nE61z1YrkLLtfWCiDDLQJI6AylW62EJHBpZ8jWt',
                      'ehRrZd1gvNCgHgrm3jr7wNP0hbn6tJxE8VusJxLH9Iybz')

    api = tweepy.API(auth)  # Access API with keys above

    geolocator = Nominatim(user_agent = "BSTwitterScraper")  # Implement GeoLocator for Posts
    eventLocation = geolocator.reverse("{}, {}".format(latitude, longitude)).address


    # Split user input keywords into Twitter API searchable format
    tags = keywords.split(" ")
    for x in tags:
        x.replace(",", "")
    keywords = keywords.replace(", ", "\"", 1)
    keywords = keywords.replace(", ", "\" \"")
    if "\"" in keywords:
        keywords += "\""

    # Send Event data to database to create a new event
    if event_id == -1:
        idevent = Twitter_parser.parseSearchData(eventName, start_date, start_time, end_date, end_time, latitude,
                                                 longitude, eventLocation, radius, tags)[1]
    else:
        idevent = event_id

    # Create an array to account for tweet duplicates
    previous_tweets = []

    # Refine keywords and geolocation for usability in Twitter API
    keywords += " -filter:retweets"
    geocode = "" + latitude + "," + longitude + "," + radius + "mi"
    for status in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keywords, geocode = geocode, tweet_mode = "extended").items(100):
        # Search through 100 tweets under the search parameters given
        while True:  # Acting do while loop for reply chains
            isRepeat = False  # Ensures duplicates are not reply chained through
            for x in previous_tweets:  # Compare the current tweet to all previous tweets to test for duplicate
                if status.id == x:  # Possibly improvement: only save previous tweet's ID and order the list for faster search
                    isRepeat = True
            if not isRepeat:  # If the tweet is not a repeat, add it to the list and gather data to send to parse
                previous_tweets.append(status.id)
                isComment = False  # Tests if a post is a reply for reply chaining
                if status.in_reply_to_status_id_str is not None:
                    isComment = True  # This post is a reply to another post
                # Create dummy values for post locations
                long = None
                lat = None
                loc = None
                # Priority listing for geo location of tweets
                if status.geo is not None:
                    # Tweet has explicit geo long/lat in its data
                    long = status.coordinates['coordinates'][0]
                    lat = status.coordinates['coordinates'][1]
                    location = geolocator.reverse("{}, {}".format(lat, long))
                    loc = location.address
                elif status.place is not None:
                    # Tweet has a named location in its data
                    loc = status.place.full_name
                    location = geolocator.geocode(loc)
                    long = location.longitude
                    lat = location.latitude
                elif status.user.location is not None:
                    # Tweet does not have geo, but the user's profile does
                    loc = status.user.location
                    location = geolocator.geocode(loc)
                    if location is not None:
                        long = location.longitude
                        lat = location.latitude
                # List of urls to send to parser
                tweet_url = []
                for x in range(len(status.entities['urls'])):
                    tweet_url.append(status.entities['urls'][x]['expanded_url'])
                # Tweet data formatted into parser's expected input
                tweet = [None, status.user.screen_name, "twitter.com", status.user.name, None, long, lat, loc, 10, None,
                         tweet_url, None, None, str(status.created_at)[:10], str(status.created_at)[11:],
                         status.full_text,
                         status.favorite_count, status.retweet_count, 0, isComment, None,
                         "https://twitter.com/twitter/status/" + status.id_str, False, status.lang,
                         0, None, None, None, None, None, None]
                Twitter_parser.parseTweet(tweet, idevent)
                if not isComment:
                    # If tweet is not a reply, break loop to end sequence
                    break
                else:
                    # If tweet is a reply, access the parent tweet and repeat to the while loop
                    try:
                        status = api.get_status(status.in_reply_to_status_id, tweet_mode="extended")
                    except:
                        print("An error occurred accessing tweets, likely a rate limit error.\nTry refining your search"
                              " and try another search in about 5 minutes.")
                        exit()
            else:
                # Exit condition when no tweets remain
                break

if __name__ == '__main__':
    Scrape("MinnesotaRiot", "Minnesota Police", "45.0", "-92.0", "100", "2021-04-21", "00:00:00", "2021-04-29", "00:00:00", -1)

