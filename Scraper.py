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


idevent=Twitter_parser.parseSearchData("SuezCanalBlocked", start_date, start_time, end_date, end_time, 30.57, 32.29, "Suez Canal", 10, tags)[1]

keyword += " -filter:retweets"
geocode = "30.57,32.29,1000mi"
for status1 in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, geocode = geocode, tweet_mode = "extended").items(100):
    isComment = False
    if status1.in_reply_to_status_id_str is not None:
        isComment = True
    tweet = [None, status1.user.screen_name, "twitter.com", status1.user.name, None, None, None, None, 24, None,
             None, None, None, str(status1.created_at)[:10], str(status1.created_at)[11:], status1.full_text,
             status1.favorite_count, status1.retweet_count, 0, isComment, None,
             "https://twitter.com/twitter/status/" + status1.id_str, False, status1.lang,
             0, None, None, None, None, None, None]
    print(tweet)
    Twitter_parser.parseTweet(tweet,idevent)


