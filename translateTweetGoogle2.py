import json
import cleanedFunction
from googletrans import Translator

input = "alltweet.json"
output = "translate.json"

all_tweet = []
f = open(input, "r")
all_tweet = json.loads(f.read())
f.close()

tweet_translate = []

all_tweet = cleanedFunction.removeRedundance(all_tweet)
translator = Translator()
global i
i = 0
count = 0

try:
    while i <= len(all_tweet):
        results = translator.translate(all_tweet[i]["text"], dest='en', src='it')
        tweet_translate.append({'text': results.text, 'date': all_tweet[i]["date"]})
        i += 1
        count += 1
        if count == 50:
            print(str(i) + "-" + str(len(all_tweet)))
            f = open(output, "w")
            f.write(json.dumps(tweet_translate))
            f.close()
            count = 0
finally:
    f = open(output, "w")
    f.write(json.dumps(tweet_translate))
    f.close()
    f = open("index.txt", "w")
    f.write(str(i))
    f.close()
    print(i)
