# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:18:21 2018
@author: shreyasjothish

Description: This file is used to interact with Twitter API
"""

import tweepy
import pandas as pd
import credentials

access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET
consumer_key = credentials.CONSUMER_KEY
consumer_secret = credentials.CONSUMER_SECRET

def authenticate():
    """
    Authenticate with Twitter API based on 
    consumer_key
    consumer_secret
    access_token
    access_token_secret
    
    Input:
    None
        
    Output:
    tweepy api object
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    return api

def fetchrelatedtweets(api, tweetid_str, itemcount=100):
    """
    Fetch related tweets based on original tweet id.
    	
    Input: 
    api - Twitter authentication object
    tweetid_str - Original tweet id string
    itemcount - Count of number of related tweets to be fetched
    There is an limit on number of tweets which can be fetched based on
    twitter account type
    	
    Output:
    DataFrame of related tweets with key informations listed below.
    1. created_at
    2. id
    3. id_str
    4. text
    5. text_range
    6. lang
    7. user_id
    8. user_id_str
    9. user_name
    10. user_screen_name
    11. retweeted - Set based on retweeted_status
    12. quoted - Set based on quoted_status
    13. polarity - Placeholder for sentiment polarity
    14. subjectivity - Placeholder for sentiment subjectivity
    	
    For more details on the fields refer:
    https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    """
    related_tweets = []
    
    for status in tweepy.Cursor(api.search, 
                                q=tweetid_str, 
                                tweet_mode='extended').items(itemcount):
        related_tweets.append(status)
	
    tweetdf = pd.DataFrame()
    	
    # Build the dataframe with key information
    tweetdf['created_at'] = list(map(lambda tweet: tweet.created_at, 
    					related_tweets))
    tweetdf['id'] = list(map(lambda tweet: tweet.id, related_tweets))
    tweetdf['id_str'] = list(map(lambda tweet: tweet.id_str, related_tweets))
    tweetdf['text'] = list(map(lambda tweet: tweet.full_text, related_tweets))
    tweetdf['text_range'] = list(map(lambda tweet: tweet.display_text_range, 
    					related_tweets))
    tweetdf['lang'] = list(map(lambda tweet: tweet.lang,
    			related_tweets))
    tweetdf['user_id'] = list(map(lambda tweet: tweet.user.id,
    			related_tweets))
    tweetdf['user_id_str'] = list(map(lambda tweet: tweet.user.id_str,
    					related_tweets))
    tweetdf['user_name'] = list(map(lambda tweet: tweet.user.name,
    					related_tweets))
    tweetdf['user_screen_name'] = list(map(
            lambda tweet: tweet.user.screen_name, related_tweets))
    tweetdf['retweeted'] = list(map(
            lambda tweet: int(hasattr(tweet,'retweeted_status')),
            related_tweets))
    tweetdf['quoted'] = list(map(
            lambda tweet: int(hasattr(tweet,'quoted_status')), related_tweets))
    tweetdf['polarity'] = list(map(lambda tweet: 0.0, 
    					related_tweets))
    tweetdf['subjectivity'] = list(map(lambda tweet: 0.0, 
    					related_tweets))
    	
    return tweetdf