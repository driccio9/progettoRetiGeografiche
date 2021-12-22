import json

import matplotlib.pyplot as plt
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import cleanedFunction

nltk.download('vader_lexicon')

# Sentiment Analysis
dir = "../sample/"
# Inserire qui il file da dare in pasto a Vader
vaderInput = "translate.json"
# Inserire qui il file che deve dare in ouput Vader
vaderOutput = dir + "TV_" + vaderInput + ".json"


def percentage(part, whole):
    return 100 * float(part) / float(whole)


# Creating PieCart
def createPieChart(positive, neutral, negative):
    labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]',
              'Negative [' + str(negative) + '%]']
    sizes = [positive, neutral, negative]
    colors = ['yellowgreen', 'blue', 'red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.style.use('default')
    plt.legend(labels)
    plt.title("Sentiment Analysis Result")
    plt.axis('equal')
    plt.show()


def vaderAnalyzer(vaderInput, vaderOutput):
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    tweet_list = []
    neutral_list = []
    negative_list = []
    positive_list = []
    sentimet_tweet = []

    f = open(vaderInput, "r")
    all_tweet = json.loads(f.read())
    f.close()

    noOfTweet = len(all_tweet)
    print(noOfTweet)
    i = 0
    count = 0

    for tweet in all_tweet:
        if count == 1000:
            print(str(noOfTweet) + "-" + str(i))
            count = 0
        text = tweet["text"]
        text = cleanedFunction.cleaned(text)
        text = cleanedFunction.remove_stopwords(text)
        # print(text)

        tweet_list.append(text)
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']

        sentimet_tweet.append(
            {'text': tweet["text"], 'date': tweet["date"], 'negative': neg, 'positive': pos, 'neutral': neu,
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

        i += 1
        count += 1

    positive = percentage(positive, noOfTweet)
    negative = percentage(negative, noOfTweet)
    neutral = percentage(neutral, noOfTweet)
    polarity = percentage(polarity, noOfTweet)
    positive = format(positive, '.1f')
    negative = format(negative, '.1f')
    neutral = format(neutral, '.1f')

    # Number of Tweets (Total, Positive, Negative, Neutral)
    tweet_list = pd.DataFrame(tweet_list)
    neutral_list = pd.DataFrame(neutral_list)
    negative_list = pd.DataFrame(negative_list)
    positive_list = pd.DataFrame(positive_list)

    print("total number: ", len(tweet_list))
    print("positive number: ", len(positive_list))
    print("negative number: ", len(negative_list))
    print("neutral number: ", len(neutral_list))

    createPieChart(positive, neutral, negative)

    f = open(vaderOutput, "w")
    f.write(json.dumps(sentimet_tweet))
    f.close()

# vaderAnalyzer(vaderInput, vaderOutput)
