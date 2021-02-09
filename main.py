import sys
import time
import tweepy
from tweepy import OAuthHandler


auth = OAuthHandler('I4l32YtrKK5XbRqEMNQbyNn1j', 'Y7pYpONITmmDyMqeoQpz2Uq5HPB7ilttI3opCtZDL1XJNYlQQx')
auth.set_access_token('3930122292-KS4T2uHvgVkbiZ5utFrzYpfrfwsMJ85lJVHi6oT',
                          '1R2pBpGZ6kXwdq8ClmK1HCvW8Mxy3Xt9i8q8q4EjifAGl')

api = tweepy.API(auth)

page = 1
while True:
    statuses = api.user_timeline("@TheOnion", page = page)
    if statuses:
        for status in statuses:
            # process status here
            print(status.text)
    else:
        # All done
        break
    page += 1  # next page
