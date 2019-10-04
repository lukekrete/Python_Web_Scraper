#-------------------------------
# Date: October 4th, 2019
# Author: Luke Krete
# Description:  Currently set up
#				scrape a twitter
#				page
#-------------------------------

#------Imports------------------
from bs4 import BeautifulSoup
import requests
#-------------------------------

all_tweets = []
url = 'https://twitter.com/TheOnion'
response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")
timeline = content.select('#timeline li.stream-item')
for tweet in timeline:
	tweet_id = tweet['data-item-id']
	tweet_text = tweet.select('p.tweet-text')[0].get_text()
	all_tweets.append({"id": tweet_id, "text": tweet_text})
	print(all_tweets)