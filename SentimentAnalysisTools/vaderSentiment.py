import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def vaderSentiment(inPathFile, outPathFile, mode='nltk'):
    valid = {'nltk', 'regex', 'none'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    positive = 0
    negative = 0
    neutral = 0
    neutral_list = []
    negative_list = []
    positive_list = []
    sentiment_tweet = []

    f = open(inPathFile, "r")
    inTweetList = json.loads(f.read())
    f.close()

    #==========================================================
    #inTweetList = inTweetList[0:2]  # per provare, da rimuovere
    #==========================================================

    noOfTweet = len(inTweetList)

    # nel caso in cui lo splitting non sia necessario
    if mode == 'none':
        for tweet in inTweetList:
            score = SentimentIntensityAnalyzer().polarity_scores(tweet['text'])
            sentiment_tweet.append(
                {
                    'text': tweet['text'],
                    'date': tweet['date'],
                    'negative': score['neg'],
                    'positive': score['pos'],
                    'neutral': score['neu'],
                    'compound': score['compound']
                }
            )
    else:
        for tweet in inTweetList:

            neg = 0
            neu = 0
            pos = 0
            comp = 0

            for sentence in tweet['cleanedSentences']:
                score = SentimentIntensityAnalyzer().polarity_scores(sentence)
                neg += score['neg'] / len(tweet['cleanedSentences'])
                neu += score['neu'] / len(tweet['cleanedSentences'])
                pos += score['pos'] / len(tweet['cleanedSentences'])
                comp += score['compound'] / len(tweet['cleanedSentences'])

            sentiment_tweet.append(
                {
                    'text': tweet["text"],
                    'date': tweet["date"],
                    'negative': neg,
                    'positive': pos,
                    'neutral': neu,
                    'compound': comp
                }
            )

            if neg > pos:
                negative_list.append(tweet["text"])
                negative += 1
            elif pos > neg:
                positive_list.append(tweet["text"])
                positive += 1
            elif pos == neg:
                neutral_list.append(tweet["text"])
                neutral += 1

        print("===INFO VADER SENTIMENT RESULT===")
        print("total number: ", noOfTweet)
        print("positive number: ", len(positive_list))
        print("negative number: ", len(negative_list))
        print("neutral number: ", len(neutral_list))
        print("==========")

    f = open(outPathFile, "w")
    f.write(json.dumps(sentiment_tweet))
    f.close()
