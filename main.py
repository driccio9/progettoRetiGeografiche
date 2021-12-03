import tweepy
import re
import cleanedFunction
import json

all_tweet = []

f = open("alltweet.json", "r")
all_tweet = json.loads(f.read())
f.close()

consumerKey = "MWdBTvrB6X2B3ykmaZ98GdQBo"
consumerSecret = "r26Ixa7suHNOjnmSy6IhmYR2buhzs2VkYZxPs5kdPMG0lqTKPG"
accessToken = "1463101705462108163-M72tQuxp7FDGTtMUiD9YcLEcKkl0w7"
accessTokenSecret = "zhn0bp4aKpXFKnAeF3ZHfkylIcoBYr46m5JlfK4TzDrgO"

auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search_tweets, q='#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio', until='2021-11-27', lang='it', locale='it', tweet_mode='extended').items(430) #items(22)

i = 0

for tweet in tweets:
    i += 1
    date = tweet.created_at.strftime("%Y-%m-%d")
    try:
        text = tweet.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        text = tweet.full_text
    all_tweet.append({'text': text, 'date': date})

#all_tweet = cleanedFunction.removeRedundance(all_tweet)
print(all_tweet)
print(i)
f = open("alltweet.json", "w")
f.write(json.dumps(all_tweet))
f.close()




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