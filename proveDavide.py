import tweepy
import re
import pandas as pd

consumerKey = "MWdBTvrB6X2B3ykmaZ98GdQBo"
consumerSecret = "r26Ixa7suHNOjnmSy6IhmYR2buhzs2VkYZxPs5kdPMG0lqTKPG"
accessToken = "1463101705462108163-M72tQuxp7FDGTtMUiD9YcLEcKkl0w7"
accessTokenSecret = "zhn0bp4aKpXFKnAeF3ZHfkylIcoBYr46m5JlfK4TzDrgO"

auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)


tweets = tweepy.Cursor(api.search_tweets, q='green pass', until='2021-11-22', lang='it', locale='it', tweet_mode='extended').items(5)

for tweet in tweets:
    try:
        print(tweet.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        print(tweet.full_text)

"""
remove_rt = lambda x: re.sub('RT @\w+: ', '', x)
tweetList = []
for tweet in tweets:
    tweetList.append(tweet.text)


tw_list = pd.DataFrame(tweetList)
tw_list['text'] = tw_list[0]

#Removing RT, Punctuation etc
remove_rt = lambda x: re.sub('RT @\w+: ', '', x)
rt = lambda x: re.sub('(@[A-Za-z0–9]+) | ([^0-9A-Za-z \t]) | (\w+:\/\/\S+)', '', x)

tw_list['text'] = tw_list['text'].map(remove_rt).map(rt)
tw_list['text'] = tw_list['text'].str.lower()

print(tw_list['text'])
"""