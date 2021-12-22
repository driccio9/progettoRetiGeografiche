import json

import tweepy

'''
all_tweet = []
f = open("alltweet.json", "r")
all_tweet = json.loads(f.read())
f.close()
'''

consumerKey = "MWdBTvrB6X2B3ykmaZ98GdQBo"
consumerSecret = "r26Ixa7suHNOjnmSy6IhmYR2buhzs2VkYZxPs5kdPMG0lqTKPG"
accessToken = "1463101705462108163-M72tQuxp7FDGTtMUiD9YcLEcKkl0w7"
accessTokenSecret = "zhn0bp4aKpXFKnAeF3ZHfkylIcoBYr46m5JlfK4TzDrgO"
safezone = False


words = [
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
]


from datetime import date

today = date.today()
d1 = today.strftime("%d")
print(d1)
day = int(d1)-7

auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)
word = 0

while True:
    fileopen = words[word] + ".json"
    all_tweet = []
    try:
        f = open(fileopen, 'r')
        all_tweet = json.loads(f.read())
        f.close()
    except IOError:
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
                # all_tweet = cleanedFunction.removeRedundance(all_tweet)
                f = open(fileopen, "w")
                f.write(json.dumps(all_tweet))
                f.close()
            safezone = True
    except Exception:
        pass
    finally:
        # all_tweet = cleanedFunction.removeRedundance(all_tweet)
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

# all_tweet = cleanedFunction.removeRedundance(all_tweet)


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
