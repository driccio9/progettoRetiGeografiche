import json
import time

from googletrans import Translator

from FunctionForCleaning.cleanedFunction import *

input = "../Tweet/alltweet.json"
output = "../Tweet/allTweetTranslate.json"

all_tweet = []
f = open(input, "r")
all_tweet = json.loads(f.read())
f.close()

tweet_translate = []
try:
    f = open(output, "r")
    tweet_translate = json.loads(f.read())
    f.close()
except:
    pass

all_tweet = removeRedundance(all_tweet)
translator = Translator()
global i
i = len(tweet_translate)
count = 0
print(i)
while i < len(all_tweet):
    try:
        cleanedText = cleaned(all_tweet[i]['text'])
        results = translator.translate(cleanedText, dest='en', src='it')
        tweet_translate.append({'text': results.text, 'date': all_tweet[i]["date"]})
        i += 1
        count += 1
        if count == 50:
            print(str(i) + "-" + str(len(all_tweet)))
            f = open(output, "w")
            f.write(json.dumps(tweet_translate))
            f.close()
            count = 0
    except:
        time.sleep(2)
        print("error found in" + str(i))
        pass

f = open(output, "w")
f.write(json.dumps(tweet_translate))
f.close()
