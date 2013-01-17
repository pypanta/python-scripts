# -*- coding: utf-8 -*-

import android
import tweepy
from sys import exit
from time import sleep, strftime

# Twitter autorizaija
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    api = tweepy.API(auth)
    print "Autorizovan kao: ", api.me().name
except tweepy.TweepError, e:
    print "Autorizacija nije uspela."
    exit(e)

# Pribavlja GPS lokaciju
droid = android.Android()
print "Započinjem lociranje..."
droid.startLocating()
sleep(20)
loc = droid.readLocation()
droid.stopLocating()

if 'gps' in loc.result:
    lat = str(loc.result['gps']['latitude'])
    lon = str(loc.result['gps']['longitude'])
else:
    lat = str(loc.result['network']['latitude'])
    lon = str(loc.result['network']['longitude'])

# Postavlja trenutno vreme
time = strftime("%a, %d %b %Y %H:%M:%S")

# Tvit poruka
msg = "%s: https://maps.google.com/?ll=%s,%s" % (time, lat, lon)

# Azurira status i ispisuje 3 zadnja tvita.
try:
    api.update_status(msg)
    tweets = api.home_timeline(count=3)
    for tweet in tweets:
        print tweet.text, "\n"
except tweepy.TweepError, e:
    exit(e)
