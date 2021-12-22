import json

import numpy as np
import pandas as pd
import text2emotion as te
from FunctionForCleaning.cleanedFunction import *


def text2emotionSentiment(inputJson, outputJson, mode='none'):
    valid = {'nltk', 'regex', 'none'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    if mode == 'none':
        df = pd.read_json(inputJson, convert_dates=False)
        emotions = df['text'].map(remove_stopwords).map(te.get_emotion).tolist()
        dataFrame = pd.concat([df, pd.DataFrame(emotions)], axis=1)
        dataFrame.to_json(outputJson, orient='records')
    else:
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



