import json
import numpy as np
import text2emotion as te


def text2emotionSentiment(inputJson, outputJson, mode='none'):
    valid = {'nltk', 'regex', 'none'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    f = open(inputJson, "r")
    inTweetList = json.loads(f.read())
    f.close()

    # ==========================================================
    #inTweetList = inTweetList[0:2]  # per provare, da rimuovere
    # ==========================================================

    outTweetList = []

    if mode == 'none':
        for tweet in inTweetList:
            emotion = te.get_emotion(tweet['cleanedText'])
            outTweetList.append(
                {
                    'text': tweet['text'],
                    'date': tweet['date'],
                    'Happy': emotion['Happy'],
                    'Angry': emotion['Angry'],
                    'Surprise': emotion['Surprise'],
                    'Sad': emotion['Sad'],
                    'Fear': emotion['Fear']
                }
            )
    else:
        for tweet in inTweetList:

            emotion = np.zeros(5)
            for sentence in tweet['cleanedSentences']:
                emotion += np.array(list(te.get_emotion(sentence).values())) / len(tweet['cleanedSentences'])

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



