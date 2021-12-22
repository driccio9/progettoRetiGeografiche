import json
import time
from googletrans import Translator
from FunctionForCleaning.cleanedFunction import *

input = "../Tweet/alltweet.json"

words = [
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
]

all_tweet = []
f = open(input, "r")
all_tweet = json.loads(f.read())
f.close()

translator = Translator()
for filepath in words:
    print(filepath)
    f = open("../Tweet/" + filepath + ".json", "r")
    all_tweet = json.loads(f.read())
    f.close()
    all_tweet = removeRedundance(all_tweet)
    output = "../TranslatedTweet/" + filepath + ".json"
    try:
        f = open(output, "r")
        tweet_translate = json.loads(f.read())
        f.close()
    except:
        tweet_translate = []
    i = len(tweet_translate)
    count = 0
    print(str(i) + "-" + len(all_tweet))
    print("traduco...")
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
