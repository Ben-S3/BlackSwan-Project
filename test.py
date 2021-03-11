import datetime
import sys
import time
import tweepy
from tweepy import OAuthHandler


auth = OAuthHandler('P3MouxIBM8paKK5WU9nq8rkDQ', '8WFkiLm136rtGfiHc8LQNpiUaQvXHrXDybUFJ55SeijbAvBzjV')
auth.set_access_token('3930122292-nE61z1YrkLLtfWCiDDLQJI6AylW62EJHBpZ8jWt',
                      'ehRrZd1gvNCgHgrm3jr7wNP0hbn6tJxE8VusJxLH9Iybz')

api = tweepy.API(auth)

keyword = input("What Keyword(s) to Search:: ")
#Insert Year, Month, and Day as Integers
start_year = input("What Start Year to Search:: ")
start_month = input("What Start Month to Search:: ")
start_day = input("What Start Day to Search:: ")
end_year = input("What End Year to Search:: ")
end_month = input("What End Month to Search:: ")
end_day = input("What End Day to Search:: ")

start_date = datetime.datetime(int(start_year), int(start_month), int(start_day), 0, 0, 0)
end_date = datetime.datetime(int(end_year), int(end_month), int(end_day), 0, 0, 0)

keyword += " -filter:retweets"
for status1 in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, tweet_mode = "extended", geocode = "32,-98,100mi").items(100):
    print("Description:: ")
    print(status1.full_text)
    print("Geo:: ")
    print(status1.geo)
    print("idLocation:: ")
    print(status1.coordinates)
    print("idUser:: ")
    print(status1.user.id)
    print("Date/Time:: ")
    print(status1.created_at)
    print("Like_Num:: ")
    print(status1.favorite_count)
    print("Repost_Num:: ")
    print(status1.retweet_count)
    print("Runtime:: ")
    print(datetime.datetime.now())
    print("\n")

