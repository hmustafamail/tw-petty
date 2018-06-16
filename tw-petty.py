#!/usr/bin/env python3
# Unfollow whoever does not follow you.
# http://docs.tweepy.org/en/v3.5.0/api.html

import tweepy
import time

# Get an API handle
consumerkey = 'get'
consumersecret = 'these'
accesstoken = 'from'
accesstokensecret = 'Twitter'

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print('Allow this to run for a long time; Twitter allows 15 API calls per 15 minutes.')

#
# find non-reciprocators
#

# get my username
me = api.me()

# get who i follow
friends = api.friends_ids(me.id)
print("i am following %i tweeters..." % len(friends))

# get who follows me
followers = api.followers_ids(me.id)
print("there are %i tweeters following me..." % len(followers))

# find all the non-reciprocators
nonreciprocators = []
for i in friends:
    if i not in followers:
        nonreciprocators.append(i)

# unfollow non-reciprocators
print("so i have %i non-reciprocators..." % len(nonreciprocators))
destructocount = 0
for i in nonreciprocators:
    time.sleep(60)
    reply = api.destroy_friendship(i)
    destructocount = destructocount + 1
    print("unfollowed %i of %i" % (destructocount, len(nonreciprocators)))

print('Done.')
