import json
from textblob import TextBlob

def textBlobSentiment(inPathFile, outPathFile, mode='none'):
    valid = {'nltk', 'regex', 'none'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    f = open(inPathFile, "r")
    inTweetList = json.loads(f.read())
    f.close()

    # ==========================================================
    #inTweetList = inTweetList[0:2]  # per provare, da rimuovere
    # ==========================================================

    textblobresult = []
    positive = 0
    negative = 0
    neutral = 0
    neutral_list = []
    negative_list = []
    positive_list = []
    noOfTweet = len(inTweetList)

    #nel caso in cui lo splitting non sia necessario
    if mode == 'none':
        for tweet in inTweetList:
            analysis = TextBlob(tweet['text'])
            textblobresult.append(
                {
                    'text': tweet['text'],
                    'date': tweet['date'],
                    'polarity': analysis.sentiment[0],
                    'subjectivity': analysis.sentiment[1]
                }
            )
    else:

        print("processo...")
        for tweet in inTweetList:

            polarity = 0
            sentiment = 0
            for sentence in tweet['cleanedSentences']:
                analysis = TextBlob(sentence)
                polarity += analysis.sentiment[0] / len(tweet['cleanedSentences'])
                sentiment += analysis.sentiment[1] / len(tweet['cleanedSentences'])

            textblobresult.append(
                {
                    'text': tweet["text"],
                    'date': tweet["date"],
                    'polarity': polarity,
                    'subjectivity': sentiment
                }
            )

            if polarity > 0:
                positive_list.append(tweet["text"])
                positive += 1
            elif polarity < 0:
                negative_list.append(tweet["text"])
                negative += 1
            else:
                neutral_list.append(tweet["text"])
                neutral += 1

        print("===INFO TEXT BLOB RESULT===")

        print("total number: ", noOfTweet)
        print("positive number: ", len(positive_list))
        print("negative number: ", len(negative_list))
        print("neutral number: ", len(neutral_list))
        print("==========")

    f = open(outPathFile, "w")
    f.write(json.dumps(textblobresult))
    f.close()
