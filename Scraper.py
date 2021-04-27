# Author: Bradley Franklin & Hope Church
# Date Created: 2/9/2021
# Date updated: 4/27/2021
# Description: Scraper of Twitter for Hard-Coded Demo of Useability

import sys
import time
import csv
import datetime
import tweepy
from tweepy import OAuthHandler
import geopy
from geopy.geocoders import Nominatim

import Twitter_parser

def Scrape():
    auth = OAuthHandler('P3MouxIBM8paKK5WU9nq8rkDQ', '8WFkiLm136rtGfiHc8LQNpiUaQvXHrXDybUFJ55SeijbAvBzjV')
    auth.set_access_token('3930122292-nE61z1YrkLLtfWCiDDLQJI6AylW62EJHBpZ8jWt',
                      'ehRrZd1gvNCgHgrm3jr7wNP0hbn6tJxE8VusJxLH9Iybz')

    api = tweepy.API(auth)

    geolocator = Nominatim(user_agent = "BSTwitterScraper")

    keyword = "Minnesota Live"
    start_year = 2021
    start_month = 4
    start_day = 18
    end_year = 2021
    end_month = 4
    end_day = 20

    tags = ["Minnesota", "protest", "riot"]

    start_date = datetime.datetime(int(start_year), int(start_month), int(start_day), 0, 0, 0)
    end_date = datetime.datetime(int(end_year), int(end_month), int(end_day), 0, 0, 0)

    start_time=start_date.strftime("%H:%M:%S")
    end_time=end_date.strftime("%H:%M:%S")

    start_date=start_date.strftime("%Y-%m-%d")
    end_date=end_date.strftime("%Y-%m-%d")

    idevent = Twitter_parser.parseSearchData("MinnesotaRiot", start_date, start_time, end_date, end_time, 45.0, -92.0, "Minnesota", 100, tags)[1]

    previous_tweets = []

    keyword += " -filter:retweets"
    geocode = "45.0,-92.0,100mi"
    for status in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, geocode = geocode, tweet_mode = "extended").items(100):
        while True:
            isRepeat = False
            for x in previous_tweets:
                if status.id == x:
                    isRepeat = True
            if not isRepeat:
                previous_tweets.append(status.id)
                isComment = False
                if status.in_reply_to_status_id_str is not None:
                    isComment = True
                long = None
                lat = None
                loc = None
                if status.geo is not None:
                    long = status.coordinates['coordinates'][0]
                    lat = status.coordinates['coordinates'][1]
                    location = geolocator.reverse("{}, {}".format(lat, long))
                    loc = location.address
                elif status.place is not None:
                    loc = status.place.full_name
                    location = geolocator.geocode(loc)
                    long = location.longitude
                    lat = location.latitude
                elif status.user.location is not None:
                    loc = status.user.location
                    location = geolocator.geocode(loc)
                    if location is not None:
                        long = location.longitude
                        lat = location.latitude
                tweet_url = []
                for x in range(len(status.entities['urls'])):
                    tweet_url.append(status.entities['urls'][x]['expanded_url'])
                tweet = [None, status.user.screen_name, "twitter.com", status.user.name, None, long, lat, loc, 10, None,
                         tweet_url, None, None, str(status.created_at)[:10], str(status.created_at)[11:],
                         status.full_text,
                         status.favorite_count, status.retweet_count, 0, isComment, None,
                         "https://twitter.com/twitter/status/" + status.id_str, False, status.lang,
                         0, None, None, None, None, None, None]
                print(tweet)
                Twitter_parser.parseTweet(tweet, idevent)
                if not isComment:
                    break
                else:
                    status = api.get_status(status.in_reply_to_status_id, tweet_mode="extended")
            else:
                break

if __name__ == '__main__':
    Scrape()

