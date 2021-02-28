import datetime
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
keyword = keyword.split()

for n in keyword:
    for status1 in tweepy.Cursor(api.search, since=start_date, until=end_date, q=n).items(30):
        print(status1.text)
        print(status1.geo)
