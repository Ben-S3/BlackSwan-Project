# Author: Bradley Franklin
# Date Created: 2/9/2021
# Date updated: 3/30/2021
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

keyword = "Monster AND Hunter"
start_year = 2021
start_month = 3
start_day = 23
end_year = 2021
end_month = 4
end_day = 2

start_date = datetime.datetime(int(start_year), int(start_month), int(start_day), 0, 0, 0)
end_date = datetime.datetime(int(end_year), int(end_month), int(end_day), 0, 0, 0)

keyword += " -filter:retweets" #Ensure no retweets included.
for status1 in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, tweet_mode = "extended").items(100): #For 100 tweets matching the search...
    isComment = False
    if status1.in_reply_to_status_id_str is not None: #Check to see if its a reply
        isComment = True
    tweet = [None, status1.user.screen_name, "twitter.com", status1.user.name, None, None, None, None, 24, None,
             None, None, None, str(status1.created_at)[:10], str(status1.created_at)[11:], status1.full_text,
             status1.favorite_count, status1.retweet_count, 0, isComment, None,
             "https://twitter.com/twitter/status/" + status1.id_str, False, status1.lang,
             0, None, None, None, None, None, None]
             #Create array of parser data
    print(tweet)
    Twitter_parser.parseTweet(tweet) #Send Data array to the Parser

