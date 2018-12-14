# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:55:20 2018
@author: shreyasjothish

Description: Helper functions
"""
import pandas as pd
from dateutil import parser

def getretweetdf(tweetdf):
    """
    Separate out retweeted records
      
    Input: 
    tweetdf - DataFrame with Re-tweet and Quoted tweet records
      
    Output: 
    DataFrame containing only Re-tweet records
    """
    retweeteddf = tweetdf[tweetdf['retweeted'] == 1]
    retweeteddf.reset_index(inplace=True)
      
    return retweeteddf


def getquotedtweetdf(tweetdf):
    """
    Separate out quoted tweets records 
      
    Input: 
    tweetdf - DataFrame with Re-tweet and Quoted tweet records
      
    Output: 
    DataFrame containing only Quoted tweet records
    """
    quoteddf = tweetdf[tweetdf['quoted'] == 1]
    quoteddf.reset_index(inplace=True)
    
    return quoteddf

def updatetotimeformat(tweetdf, colname):
    """
    Update DataFrame column from string to datatime  
    
    Input: 
    column - DataFrame column in string format
        
    Output: 
    DataFrame column in datatime format 
    """
    for i in range(len(tweetdf)):
        tweetdf.loc[i,colname] = parser.parse(tweetdf.loc[i,colname])
      
    return tweetdf

