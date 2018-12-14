# tweetsentimenttimeline
To what extent the sentiment of the people's response is influenced by original tweet from the Trump?

**Major Dependency:**:
* python-datautil
> https://anaconda.org/conda-forge/python-dateutil
* Tweepy, An easy-to-use Python library for accessing the Twitter API.
> https://anaconda.org/conda-forge/tweepy
* TextBlob, Simplified Text Processing
> https://textblob.readthedocs.io/en/dev/install.html

**twittersentiment.py:**
* Run this file to create tweetdataset based on original tweet from Trump.
* tweetsummary.csv file shall contain sentiment analysis done on individual Trump tweets.
* tweetdatasetXX.csv files shall be contain sentiment analysis done on related tweets to Trump's tweet.
* Each tweetdatasetXX.csv file corresponds to one row of tweetsummary.csv.

**twittersentimenttimeline.py:**
* Run this file to create consolidated sentiment summary based on original tweet from Trump.
* tweetsummaryconsolidated.csv file shall contain consolidated sentiment analysis done on related tweets to Trump's tweet.

**tweetsentimenttimeline.ipynb:**
* Run this file for analysis and visualization using Plotly.
* Update your Plotly username and api_key.
* Uses tweetsummaryconsolidated.csv, positivetweetdataset.csv and negativetweetdataset.csv.

**credentials.py:**
* Update your Twitter ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY and CONSUMER_SECRET.

**/data:**
* tweetsummaryconsolidated.csv, positivetweetdataset.csv and negativetweetdataset.csv can be used for reproducing the test results.
* positivetweetdataset.csv correponds to index 1 entry in tweetsummary.csv with quotedcount = 167.
* negativetweetdataset.csv correponds to index 2 entry in tweetsummary.csv with quotedcount = 147.
* User information in positivetweetdataset.csv and negativetweetdataset.csv are anonymized for privacy.

