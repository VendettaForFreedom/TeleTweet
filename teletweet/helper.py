#!/usr/bin/env python3
# coding: utf-8

# TeleTweet - helper.py
# 2023-05-20  22:32

import json
import logging
from base64 import b64decode
from config import AUTH_STRING

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "auth.json"
abs_file_path = os.path.join(script_dir, rel_path)


def get_auth_data(chat_id: int) -> dict:
    chat_id = str(chat_id)
    data = json.load(open(abs_file_path, "r"))
    return data.get(str(chat_id), {})


def sign_in(chat_id: int, auth_string):
    if auth_string == AUTH_STRING:
        logging.info("Adding user oauth token...")
        auth_dict = "1234567890"
        data = json.load(open(abs_file_path, "r"))
        data[str(chat_id)] = json.loads(auth_dict)
        json.dump(data, open(abs_file_path, "w"))
        return True
    return False


def sign_off(chat_id: str):
    logging.info("Deleting user oauth token...")
    data = json.load(open(abs_file_path, "r"))
    data.pop(str(chat_id), None)
    json.dump(data, open(abs_file_path, "w"))
