#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import time

#Import configs
from config import *



#Banner
if banner_check == True:
    with open("banner") as f:
        banner = f.read()
        print(banner)

#input target
target= input("Enter target:")


#response
response = requests.post("https://open-api.trovo.live/openplatform/channels/id",headers={"Accept": "application/json","Client-ID": clinet_id},json={"username":target})


#Check if request was valid
if 400 == response.status_code :
    print("Error proceeding request")
    quit()


#convert data to json format
data = json.loads(response.text)


#target
if target_check == True:
    print("Target username:", data['username'])


#title
if live_title_check == True:
    print("Live title:", data['live_title'])


#category
if category_check == True:
    print("Category:", data['category_name'])


#followers
if followers_check == True:
    print("Followers:", data['followers'])


#viewers
if current_viewers_check == True:
    print("Current viewers:", data['current_viewers'])

#subscribers
if subscriber_check == True:
    print("Subscribers:", data['subscriber_num'])

#started live
if start_check == True:
    start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(data['started_at'])))
    print("Started live at:", start)


#is live
if is_live_check == True:
    if data['is_live'] == True:
        check = "Streaming"

    elif data['is_live'] == False:
        check = "Offline"

    print("Live status:", check)
