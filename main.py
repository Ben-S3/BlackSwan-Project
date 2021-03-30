import sys
import time
import datetime
import tweepy
import csv
from tweepy import OAuthHandler

import Twitter_parser


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

f = open("D:/School/ComputerProject/test_file.csv", "w", encoding = "utf-8", newline = "")
writer = csv.writer(f)
header = ["Title", "User_ID", "Username", "Date", "Time", "Description", "Likes", "Comments", "Dislikes", "Is_Comment", "Parent_ID", "URL", "Issensitive", "Language", "Shares", "ID"]
writer.writerow(header)

#Tweet objects to be sent to parser to sql insert into database
keyword += " -filter:retweets"
#geocode = "32,-98,100mi"
for status1 in tweepy.Cursor(api.search, since=start_date, until=end_date, q=keyword, tweet_mode = "extended").items(100):
    print("Description:: ")
    print(status1.full_text)
    if status1.full_text.rfind("https://") != -1:
        print("HAS LINK")
    #if len(status1.entities.get('media', [])) > 1:
    #    print("HAS LINK!") Not sure how to work?
    print("Geo:: ")
    print(status1.geo)
    isComment = False
    if status1.in_reply_to_status_id_str is not None:
        print("REPLY")
        isComment = True
    #Get reply, if it is, get the parent and send it first, go up the list
    print("URL:: ")
    print("https://twitter.com/twitter/status/" + status1.id_str)
    #Find how to get # of replies
    print("User:: ")
    print(status1.user.screen_name)
    print("idLocation:: ")
    print(status1.coordinates)
    print("idUser:: ")
    print(status1.user.id)
    print("Date/Time:: ")
    print(status1.created_at)
    print(str(status1.created_at)[:10])
    print(str(status1.created_at)[11:])
    print("Like_Num:: ")
    print(status1.favorite_count)
    print("Repost_Num:: ")
    print(status1.retweet_count)
    print("Langauge:: ")
    print(status1.lang)
    print("\n")
    #Include User ID
    data = ["N/A", status1.user.id, status1.user.name, str(status1.created_at)[:10], str(status1.created_at)[11:], status1.full_text, status1.favorite_count, "N/A", "N/A", isComment, "N/A", "https://twitter.com/twitter/status/" + status1.id_str, False, status1.lang, status1.retweet_count, status1.id_str]
    writer.writerow(data)
    print("Success\n")
    tweet = [None, status1.user.name, "twitter.com", status1.user.screen_name, None, None, None, None, 24, None,
             None, None, None, str(status1.created_at)[:10], str(status1.created_at)[11:], status1.full_text,
             status1.favorite_count, status1.retweet_count, 0, isComment, None,
             "https://twitter.com/twitter/status/" + status1.id_str, False, status1.lang,
             0, None, None, None, None, None, None]
    print(tweet)
    Twitter_parser.parseTweet(tweet)

#geo location priority 1. Tweet itself 2. Profile Geo 3. None
#pass an array of objects (refined to these attributes)
#scrape uses loop, parse once per loop
f.close()

