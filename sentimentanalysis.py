# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 04:14:29 2018
@author: shreyasjothish

Description: This file is performs sentiment analysis based on Textblob
"""
from textblob import TextBlob
import pandas as pd

def sentimentanalysis(quoteddf):
    """
    Perform sentiment analysis on Quoted DataFrame
    
    Input:
    quoteddf - DataFrame for sentiment analysis
        
    Output:
    quoteddfcopy - DataFrame updated with polarity and subjectivity
    """    
    quoteddfcopy = quoteddf.copy()

    for i in range(0, len(quoteddf)):
      polarity, subjectivity = calculatesentiment(quoteddfcopy['text'][i])
      
      # Update polarity and subjectivity
      quoteddfcopy.loc[i, 'polarity'] = polarity
      quoteddfcopy.loc[i, 'subjectivity'] = subjectivity
      
    return quoteddfcopy


def calculatesentiment(text):
    """
    Calculate polarity and subjectivity
    
    Input:
    text - text for which polarity and subjectivity needs to be calculated
        
    Output:
    (polarity, subjectivity)
    """
    blob = TextBlob(text)
      
    if blob.detect_language() != 'en':
        try:
            blob = blob.translate(to="en")
        except:
          print("Translation error:",blob.detect_language())
          print(blob)
          
    blob.correct()
      
    return (float(blob.sentiment.polarity), 
            float(blob.sentiment.subjectivity))