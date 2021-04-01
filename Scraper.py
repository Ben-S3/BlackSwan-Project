# Author: Bradley Franklin & Hope Church
# Date Created: 2/9/2021
# Date updated: 4/1/2021
# Description: Scraper of Twitter for Hard-Coded Demo of Useability

import sys
import time
import csv
import datetime
import tweepy
from tweepy import OAuthHandler

import Twitter_parser


auth = OAuthHandler('P3MouxIBM8paKK5WU9nq8rkDQ', '8WFkiLm136rtGfiHc8LQNpiUaQvXHrXDybUFJ55SeijbAvBzjV')
auth.set_access_token('3930122292-nE61z1YrkLLtfWCiDDLQJI6AylW62EJHBpZ8jWt',
                      'ehRrZd1gvNCgHgrm3jr7wNP0hbn6tJxE8VusJxLH9Iybz')

api = tweepy.API(auth)

keyword = "Suez Canal Evergreen"
start_year = 2021
start_month = 3
start_day = 26
end_year = 2021
end_month = 4
end_day = 2

tags = ["Suez", "Canal", "Evergreen", "Ever", "Given"]

start_date = datetime.datetime(int(start_year), int(start_month), int(start_day), 0, 0, 0)
end_date = datetime.datetime(int(end_year), int(end_month), int(end_day), 0, 0, 0)

start_time=start_date.strftime("%H:%M:%S")
end_time=end_date.strftime("%H:%M:%S")

start_date=start_date.strftime("%Y-%m-%d")
end_date=end_date.strftime("%Y-%m-%d")

Twitter_parser.parseSearchData("SuezCanalBlocked", start_date.date, start_date.time, end_date.date, end_date.time, 30.57, 32.29, "Suez Canal", 100, tags)[1]

keyword += " -filter:retweets"
geocode = "30.57,32.29,100mi"
for status in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, geocode = geocode, tweet_mode = "extended").items(100):
    isComment = False
    if status.in_reply_to_status_id_str is not None:
        isComment = True
    tweet = [None, status.user.screen_name, "twitter.com", status.user.name, None, None, None, None, 10, None,
             None, None, None, str(status.created_at)[:10], str(status.created_at)[11:], status.full_text,
             status.favorite_count, status.retweet_count, 0, isComment, None,
             "https://twitter.com/twitter/status/" + status.id_str, False, status.lang,
             0, None, None, None, None, None, None]
    print(tweet)
    Twitter_parser.parseTweet(tweet,idevent)

Twitter_parser.parseSearchData("SuezCanalBlocked", start_date.date, start_date.time, end_date.date, end_date.time, 40.71, -74.00, "New York City", 10, tags)[1]
geocode = "40.71,-74.00,10mi"
for status in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, geocode = geocode, tweet_mode = "extended").items(100):
    isComment = False
    if status.in_reply_to_status_id_str is not None:
        isComment = True
    tweet = [None, status.user.screen_name, "twitter.com", status.user.name, None, None, None, None, 10, None,
             None, None, None, str(status.created_at)[:10], str(status.created_at)[11:], status.full_text,
             status.favorite_count, status.retweet_count, 0, isComment, None,
             "https://twitter.com/twitter/status/" + status.id_str, False, status.lang,
             0, None, None, None, None, None, None]
    print(tweet)
    Twitter_parser.parseTweet(tweet,idevent)

Twitter_parser.parseSearchData("SuezCanalBlocked", start_date.date, start_date.time, end_date.date, end_date.time, 29.76, -95.36, "Houston, Texas", 10, tags)[1]
geocode = "29.76,-95.36,10mi"
for status in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, geocode = geocode, tweet_mode = "extended").items(100):
    isComment = False
    if status.in_reply_to_status_id_str is not None:
        isComment = True
    tweet = [None, status.user.screen_name, "twitter.com", status.user.name, None, None, None, None, 10, None,
             None, None, None, str(status.created_at)[:10], str(status.created_at)[11:], status.full_text,
             status.favorite_count, status.retweet_count, 0, isComment, None,
             "https://twitter.com/twitter/status/" + status.id_str, False, status.lang,
             0, None, None, None, None, None, None]
    print(tweet)
    Twitter_parser.parseTweet(tweet,idevent)

