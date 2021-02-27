import sys
import time
import tweepy
from tweepy import OAuthHandler


auth = OAuthHandler('I4l32YtrKK5XbRqEMNQbyNn1j', 'Y7pYpONITmmDyMqeoQpz2Uq5HPB7ilttI3opCtZDL1XJNYlQQx')
auth.set_access_token('3930122292-KS4T2uHvgVkbiZ5utFrzYpfrfwsMJ85lJVHi6oT',
                          '1R2pBpGZ6kXwdq8ClmK1HCvW8Mxy3Xt9i8q8q4EjifAGl')

api = tweepy.API(auth)

user = input("What User to Search:: ")
#Insert 1(one) word as a keyword search
keyword = input("What Keyword to Search:: ")
#Insert Year, Month, and Day as Integers
start_year = input("What Start Year to Search:: ")
start_month = input("What Start Month to Search:: ")
start_day = input("What Start Day to Search:: ")
end_year = input("What End Year to Search:: ")
end_month = input("What End Month to Search:: ")
end_day = input("What End Day to Search:: ")

start_date = datetime.datetime(int(start_year), int(start_month), int(start_day), 0, 0, 0)
end_date = datetime.datetime(int(end_year), int(end_month), int(end_day), 0, 0, 0)

page = 1  # One Page includes 20 tweets.
while True:
    statuses = api.user_timeline(user, page = page)  # Select user and their timeline on a certain "page".
    if statuses:  # As long as there are tweets on this page...
        for status in statuses:  # Loop through the tweets...
            if(status.created_at < start_date):
                exit(0)  # Exit program if search date is over
            if(keyword in status.text and status.created_at < end_date and status.created_at > start_date):
                print(status.text)  # And print their text
                print(status.created_at)
    else:
        # All done
        break
    page += 1  # Next page
