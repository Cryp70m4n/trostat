#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import time

#Exporting configs
from config import *

c = TrostatConfig.ParseConfig("config.json")


#Banner
if c.banner_check == True:
    with open("banner") as f:
        banner = f.read()
        print(banner)

#input target
target= input("Enter target:")


#response
response = requests.post("https://open-api.trovo.live/openplatform/channels/id",headers={"Accept": "application/json","Client-ID": c.client_id},json={"username":target})


if 400 == response.status_code :
    print("Error proceeding request")
    quit()


#convert data to json format
data = json.loads(response.text)


#target
if c.target_check == True:
    print("Target username:", data['username'])


#title
if c.live_title_check == True:
    print("Live title:", data['live_title'])


#category
if c.category_check == True:
    print("Category:", data['category_name'])


#followers
if c.followers_check == True:
    print("Followers:", data['followers'])


#viewers
if c.current_viewers_check == True:
    print("Current viewers:", data['current_viewers'])

#subscribers
if c.subscriber_check == True:
    print("Subscribers:", data['subscriber_num'])

#started live
if c.start_check == True:
    start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(data['started_at'])))
    print("Started live at:", start)


#is live
if c.is_live_check == True:
    if data['is_live'] == True:
        check = "Streaming"

    elif data['is_live'] == False:
        check = "Offline"

    print("Live status:", check)
