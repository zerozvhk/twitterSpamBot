/*
 * Copyright 2022 ZeroZhvk
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 */

import requests
import os
import tweepy
import random
import base64
from time import sleep

USERNAME = '%%TARGET USERNAME%%'# handle of the account to reply to
MESSAGE = '%% YOUR REPLY MESSAGE %%' # reply message to send
SLEEP_TIMEOUT = 10 # timeout between attempts

def twitter_api():
	auth = tweepy.OAuth1UserHandler(
   	"%% YOUR TWITTER APP API KEY %%", "%% YOUR TWITTER APP API KEY SECRET %%",
   	"%% YOUR TWITTER ACCESS KEY SECRET%%", "%% YOUR TWITTER ACCESS KEY SECRET%%"
	)
	api = tweepy.API(auth)
	return api

api = twitter_api()

tweet_list= api.user_timeline(screen_name = USERNAME, count=1)
tweet= tweet_list[0]
recent_id = tweet.id
while True:
  recent_posts = api.user_timeline(screen_name = USERNAME, since_id=recent_id, include_rts = True)
  if recent_posts:
    for recent_post in recent_posts:
      print(recent_post)
      recent_id = recent_post.id
      api.update_status(status = MESSAGE, in_reply_to_status_id = recent_id, auto_populate_reply_metadata=True)
  sleep(SLEEP_TIMEOUT) 

