import json

import numpy as np
import pandas as pd
import text2emotion as te

from FunctionForCleaning.cleanedFunction import *


#il testo deve essere tradotto in linugua inglese
def text2emotion(inputJson, outputJson):
    df = pd.read_json(inputJson, convert_dates=False)
    emotions = df['text'].map(remove_stopwords).map(te.get_emotion).tolist()
    dataFrame = pd.concat([df, pd.DataFrame(emotions)], axis=1)
    dataFrame.to_json(outputJson, orient='records')


def text2emotionSentence(inputJson, outputJson, mode:str):
    valid = {'nltk', 'regex'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    f = open(inputJson, "r")
    inTweetList = json.loads(f.read())
    f.close()

    outTweetList = []
    for tweet in inTweetList:

        if mode == 'nltk':
            sentenceList = nltkSentenceSplit(tweet['text'])
        else:
            sentenceList = regexSentenceSplit(tweet['text'])

        emotion = np.zeros(5)
        for sentence in sentenceList:
            emotion += np.array(list(te.get_emotion(remove_stopwords(sentence)).values())) / len(sentenceList)

        norm = np.linalg.norm(emotion, ord=1)

        if norm != 0:
            emotion /= np.linalg.norm(emotion, ord=1)

        outTweetList.append(
            {
                'text': tweet['text'],
                'date': tweet['date'],
                'Happy': emotion[0],
                'Angry': emotion[1],
                'Surprise': emotion[2],
                'Sad': emotion[3],
                'Fear': emotion[4]
            }
        )

    f = open(outputJson, "w")
    f.write(json.dumps(outTweetList))
    f.close()

"""
#Prova#########
df = pd.read_json(r'alltweet.json',  convert_dates=False)
text2emotion(df, r'sample/text2emotionAllTweet.json')
################
"""

"""
prefix = r'sample\TRANSLATED_'
postfix = '.json'
outPrefix = r'sample\T2E_'

words = [
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)'
]

for i in range(0,len(words)):
    df = pd.read_json(prefix+words[i]+postfix, convert_dates=False)
    text2emotion(df, outPrefix+words[i]+postfix)
"""


