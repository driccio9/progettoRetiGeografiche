import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from FunctionForCleaning.cleanedFunction import *


def vaderSentiment(inPathFile, outPathFile, mode='nltk'):
    valid = {'nltk', 'regex', 'none'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)
    nltk.download('vader_lexicon')

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

    noOfTweet = len(inTweetList)

    # nel caso in cui lo splitting non sia necessario
    if mode == 'none':
        for tweet in inTweetList:
            score = SentimentIntensityAnalyzer().polarity_scores(remove_stopwords(tweet['text']))
            sentiment_tweet.append(
                {
                    'text': tweet['text'],
                    'date': tweet['date'],
                    'negative': score['neg'],
                    'positive': score['neu'],
                    'neutral': score['pos'],
                    'compound': score['compound']
                }
            )
    else:
        for sentence in inTweetList:
            if mode == 'nltk':
                sentenceList = nltkSentenceSplit(sentence['text'])

            if mode == 'regex':
                sentenceList = regexSentenceSplit(sentence['text'])

            neg = 0
            neu = 0
            pos = 0
            comp = 0
            for text in sentenceList:
                score = SentimentIntensityAnalyzer().polarity_scores(remove_stopwords(text))
                neg += score['neg'] / len(sentenceList)
                neu += score['neu'] / len(sentenceList)
                pos += score['pos'] / len(sentenceList)
                comp += score['compound'] / len(sentenceList)

            sentiment_tweet.append(
                {'text': sentence["text"], 'date': sentence["date"], 'negative': neg, 'positive': pos, 'neutral': neu,
                 'compound': comp})

            if neg > pos:
                negative_list.append(text)
                negative += 1
            elif pos > neg:
                positive_list.append(text)
                positive += 1
            elif pos == neg:
                neutral_list.append(text)
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
