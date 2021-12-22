import json
import signal

import tweepy

all_tweet = []
f = open("Tweet/alltweet.json", "r")
all_tweet = json.loads(f.read())
f.close()

consumerKey = "MWdBTvrB6X2B3ykmaZ98GdQBo"
consumerSecret = "r26Ixa7suHNOjnmSy6IhmYR2buhzs2VkYZxPs5kdPMG0lqTKPG"
accessToken = "1463101705462108163-M72tQuxp7FDGTtMUiD9YcLEcKkl0w7"
accessTokenSecret = "zhn0bp4aKpXFKnAeF3ZHfkylIcoBYr46m5JlfK4TzDrgO"
safezone = False


def handler(signum, frame):
    if safezone:
        global all_tweet
        f = open("../alltweet.json", "w")
        f.write(json.dumps(all_tweet))
        f.close()
        print('Ctrl+Z pressed')


signal.signal(signal.SIGINT, handler)

day = "21"
month = "12"

auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = tweepy.Cursor(api.search_tweets,
                       q='#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio',
                       until='2021-' + month + '-' + day, lang='it', locale='it', tweet_mode='extended').items(
    100000)  # items(22)

i = 0
count = 0

try:
    for tweet in tweets:
        i += 1
        count += 1
        date = tweet.created_at.strftime("%Y-%m-%d")
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:  # Not a Retweet
            text = tweet.full_text
        all_tweet.append({'text': text, 'date': date})
        if count == 1000:
            print(i)
            count = 0
            f = open("../alltweet.json", "w")
            f.write(json.dumps(all_tweet))
            f.close()
        safezone = True
except Exception:
    pass
finally:
    f = open("../alltweet.json", "w")
    f.write(json.dumps(all_tweet))
    f.close()
