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
SOURCE_CHANNEL_ID = os.getenv("SOURCE_CHANNEL_ID", "-1001999856193")
GROUP_ID = os.getenv("GROUP_ID", "")
# AUTH_STRING = os.getenv("AUTH_STRING", "")

FEEDBACK = "\n\nنظرات و پیشنهادات خودتون رو برامون تو گروه بنویسین:\n@FreeVPNHomesDiscussion\n\nتوییتر:\nhttps://twitter.com/FreeVPNHomes"
TODAY_CONFIG = "کانفیگ های امروز"
CHANNEL_URL = """\n\nhttps://t.me/FreeVPNHomes\n\n"""
CHANNEL = """\n\n@FreeVPNHomes\n\n"""
SIGN = """به امید آزادی #توماج_صالحی\n#مهسا_امینی\n#آرمیتا_گراوند"""
LAST_MESSAGE = ":\nhttps://t.me/FreeVPNHomesConfigs/"

tweet_format = "https://twitter.com/{screen_name}/status/{id}"
# remove ALLOW_USERS white spaces then split by comma
ALLOW_USERS = os.getenv("ALLOW_USERS", "").replace(" ", "").split(",") if os.getenv("ALLOW_USERS", "") else [""]
