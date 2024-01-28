#!/usr/local/bin/python3
# coding: utf-8

# TeleTweet - config.py
# 10/22/20 16:20
#

__author__ = "Benny <benny.think@gmail.com>"

import os

BOT_TOKEN = os.getenv("TOKEN", "")
APP_ID = int(os.getenv("APP_ID", ""))
APP_HASH = os.getenv("APP_HASH", "")

CONSUMER_KEY = os.getenv("CONSUMER_KEY", "")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET", "")
ACCESS_KEY = os.getenv("ACCESS_KEY", "")
ACCESS_SECRET = os.getenv("ACCESS_SECRET", "")
CONFIG_CHANNEL_ID = os.getenv("CONFIG_CHANNEL_ID", "")
CHANNEL_ID = os.getenv("CHANNEL_ID", "")
# AUTH_STRING = os.getenv("AUTH_STRING", "")

tweet_format = "https://twitter.com/{screen_name}/status/{id}"
