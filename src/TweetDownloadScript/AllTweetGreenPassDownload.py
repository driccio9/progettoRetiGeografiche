import json
import signal
import tweepy

alltweetjsonfilepath = "../Tweet/alltweet.json"

all_tweet = []
f = open(alltweetjsonfilepath, "r")
all_tweet = json.loads(f.read())
f.close()

consumerKey = "yourConsumerKey"
consumerSecret = "yourConsumerSecret"
accessToken = "yourAccessToken"
accessTokenSecret = "yourAccessTokenSecret"
safezone = False

def handler(signum, frame):
    if safezone:
        global all_tweet
        global alltweetjsonfilepath
        f = open(alltweetjsonfilepath, "w")
        f.write(json.dumps(all_tweet))
        f.close()
        print('Ctrl+Z pressed')
        exit()


signal.signal(signal.SIGINT, handler)

day = "27"
month = "12"

auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = tweepy.Cursor(api.search_tweets,
                       q='#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio',
                       until='2021-' + month + '-' + day, lang='it', locale='it', tweet_mode='extended').items(
    100000)

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
            print({'text': text, 'date': date})
            print(i)
            count = 0
            f = open(alltweetjsonfilepath, "w")
            f.write(json.dumps(all_tweet))
            f.close()
        safezone = True
except Exception:
    pass
finally:
    f = open(alltweetjsonfilepath, "w")
    f.write(json.dumps(all_tweet))
    f.close()
