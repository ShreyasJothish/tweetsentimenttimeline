# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:34:44 2018
@author: shreyasjothish

Description: This is the main file to fetch of tweet and its corresponding 
quoted tweets.
"""

import pandas as pd
import twitterapi
import util
import sentimentanalysis
import time

api = twitterapi.authenticate()

# Entity refers to person or thing whose tweets we are interested in
entity = api.get_user('realDonaldTrump')

# Verify basic information
print("id:", entity.id)
print("id_str:", entity.id_str)
print("name:", entity.name)
print("screen_name:", entity.screen_name)
print("followers_count:", entity.followers_count)

# Get recent status/tweet of entity
result = api.user_timeline(id=entity.id, count=10, tweet_mode='extended')

# tweet is a tweepy.models.Status object
# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
tweetsummary = []
count = 0

for tweet in result:
    print("======================"+str(count)+"==============================")
    # Fetch related tweets for building the summary
    print(tweet.created_at)
    print(tweet.id_str)
    print(tweet.full_text)
    
    tweetdf = pd.DataFrame() 
    tweetdf = twitterapi.fetchrelatedtweets(api, tweet.id_str, itemcount=200)
    
    retweetcount = len(tweetdf[tweetdf['retweeted'] == 1])
    quotedcount = len(tweetdf[tweetdf['quoted'] == 1])
    
    ratio = 0
    if retweetcount != 0:
        ratio = quotedcount/retweetcount
    
    # Caclculate tweet sentiment
    polarity, subjectivity = sentimentanalysis.calculatesentiment(tweet.full_text)
    
    # Perform sentiment analysis on quoted tweets
    quoteddf = util.getquotedtweetdf(tweetdf)  
    
    count += 1

    quoteddfupdated = sentimentanalysis.sentimentanalysis(quoteddf)
    quoteddfupdated.to_csv("tweetdataset"+str(count)+".csv")
    
    mean_quoted_polarity = quoteddfupdated.polarity.mean()
    mean_quoted_subjectivity = quoteddfupdated.subjectivity.mean()
    
    # Update with key information
    tweetsummary.append({"created_at": tweet.created_at,
                       "id": tweet.id,
                       "id_str": tweet.id_str, 
                       "text": tweet.full_text,
                       "text_range": tweet.display_text_range,
                       "lang": tweet.lang,
                       "polarity": polarity,
                       "subjectivity": subjectivity,
                       "totalcount": len(tweetdf), 
                       "retweetcount": retweetcount,
                       "quotedcount": quotedcount,
                       "ratio": ratio,
                       "mean_quoted_polarity": mean_quoted_polarity,
                       "mean_quoted_subjectivity": mean_quoted_subjectivity})
    print("=============================Sleep 60 sec =========================")
    time.sleep(60)
    print("==================================================================")

tweetsummarydf = pd.DataFrame(tweetsummary)
tweetsummarydf.to_csv("tweetsummary.csv")


