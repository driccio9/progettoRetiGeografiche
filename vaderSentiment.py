import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from Tools.scripts.dutree import display
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS

import cleanedFunction

# Sentiment Analysis

# Inserire qui il file da dare in pasto a Vader
vaderInput = "alltweet.json"


def percentage(part, whole):
    return 100 * float(part) / float(whole)


# Function to Create Wordcloud
def create_wordcloud(text):
    mask = np.array(Image.open("cloud.png"))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",
                   mask=mask,
                   max_words=3000,
                   stopwords=stopwords,
                   repeat=True
                   )
    wc.generate(str(text))
    wc.to_file("wc.png")
    print("Word Cloud Saved Successfully")
    path = "wc.png"
    display(Image.open(path))


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


positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []
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
    analysis = TextBlob(text)
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity

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
# WIP - create_wordcloud(tweet_list["text"].values)
