import json

from textblob import TextBlob

from FunctionForCleaning.cleanedFunction import *


def textBlobSentiment(inPathFile, outPathFile, mode='nltk'):
    valid = {'nltk', 'regex'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    f = open(inPathFile, "r")
    inTweetList = json.loads(f.read())
    f.close()

    textblobresult = []
    positive = 0
    negative = 0
    neutral = 0
    neutral_list = []
    negative_list = []
    positive_list = []
    noOfTweet = len(inTweetList)

    print("processo...")
    for sentence in inTweetList:
        if mode == 'nltk':
            sentenceList = nltkSentenceSplit(sentence['text'])

        if mode == 'regex':
            sentenceList = regexSentenceSplit(sentence['text'])

        polarity = 0
        sentiment =0
        for text in sentenceList:
            analysis = TextBlob(text)
            polarity += analysis.sentiment[0] / len(sentenceList)
            sentiment += analysis.sentiment[1] / len(sentenceList)

        textblobresult.append({'text': sentence["text"], 'date': sentence["date"], 'polarity': polarity, 'subjectivity': sentiment})

        if polarity > 0:
            positive_list.append(text)
            positive += 1
        elif polarity < 0:
            negative_list.append(text)
            negative += 1
        else:
            neutral_list.append(text)
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
