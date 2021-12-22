import text2emotion as te
import pandas as pd
import json
from cleanedFunction import *
import numpy as np


#il testo deve essere tradotto in linugua inglese
def text2emotion(dataFrame:pd.DataFrame, outPathFile):
    emotions = dataFrame['text'].map(te.get_emotion).tolist()
    dataFrame = pd.concat([dataFrame, pd.DataFrame(emotions)], axis=1)
    dataFrame.to_json(outPathFile, orient='records')


def text2emotionSentence(inPathFile, outPathFile, mode='nltk'):
    valid = {'nltk', 'regex'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    f = open(inPathFile, "r")
    inTweetList = json.loads(f.read())
    f.close()

    outTweetList = []
    for tweet in inTweetList:

        if mode == 'nltk':
            sentenceList = nltkSentenceSplit(tweet['text'])

        emotion = np.zeros(5)
        for sentence in sentenceList:
            emotion += np.array(list(te.get_emotion(remove_stopwords(sentence)).values())) / len(sentenceList)

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


    f = open(outPathFile, "w")
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


