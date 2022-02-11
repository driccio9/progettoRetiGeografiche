import json
import tweepy

consumerKey = "yourConsumerKey"
consumerSecret = "yourConsumerSecret"
accessToken = "yourAccessToken"
accessTokenSecret = "yourAccessTokenSecret"
safezone = False

words = [
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
]

from datetime import date

today = date.today()
d1s = today.strftime("%d")
d1 = int(d1s) + 1
print(d1)
day = int(d1) - 7

auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)
word = 0
dir = "../../data/Tweet/"

while True:
    fileopen = dir + words[word] + ".json"
    try:
        f = open(fileopen, 'r')
        all_tweet = json.loads(f.read())
        f.close()
    except IOError:
        all_tweet = []
        pass

    tweets = tweepy.Cursor(
        api.search_tweets,
        q=words[word],
        until='2021-12' + '-' + str(day),
        lang='it',
        locale='it',
        tweet_mode='extended').items(70000)  # items(22)

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
                f = open(fileopen, "w")
                f.write(json.dumps(all_tweet))
                f.close()
            safezone = True
    except Exception:
        pass
    finally:
        f = open(fileopen, "w")
        f.write(json.dumps(all_tweet))
        f.close()
        print(str(i) + " saved " + str(day) + "-" + str(word))

    if day < int(d1):
        day += 1
        print(day)
    else:
        day = 1
        word += 1
        print(str(word) + "\n")
        if word >= len(words):
            print(str(word) + "end")
            break
