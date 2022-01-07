import re
import html
import nltk
import json

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


x = 'RT @fausername1: @fakeusername2 just bought 30.6 BTC from https://fakeesceafafa.com &amp; I am hating the crash\n Hope it recovers so... '
y = "Barton did feebly change man she afford square add. Want eyes by neat so just must. Past draw tall up face show rent oh mr. Required is debating extended wondered as do. New get described applauded incommode shameless out extremity but. Resembled at perpetual no believing is otherwise sportsman. Is do he dispatched cultivated travelling astonished. Melancholy am considered possession on collecting everything."


def cleaned(text):
    text = re.sub(
        "(#\S+)|(RT @\w+:)|(@\S+)|([+-]?[0-9]+)|([-+]?[0-9]*.[0-9]+)|(http\S+)|(\.\.\.)",
        '',
        html.unescape(text)
    )
    return text.lower()


def collapse_list_to_string(string_list):
    # This is to join back together the text data into a single string
    return ' '.join(string_list)


def remove_stopwords(text_data: str):
    text_tokens = word_tokenize(text_data)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    return collapse_list_to_string(tokens_without_sw)


def regexSentenceSplit(text: str):
    return re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)


def nltkSentenceSplit(text: str):
    return nltk.sent_tokenize(text)


def removeRedundance(l: list):
    return [dict(t) for t in {tuple(d.items()) for d in l}]


def preProcessing(inputJson, outputJson, mode):
    valid = {'nltk', 'regex', 'none'}
    if mode not in valid:
        raise ValueError("mode must be one of %r." % valid)

    f = open(inputJson, "r")
    inTweetList = json.loads(f.read())
    f.close()

    outTweetList = []

    for tweet in inTweetList:
        if mode == 'none':
            outTweetList.append(
                {
                    'text': tweet['text'],
                    'date': tweet['date'],
                    'cleanedText': remove_stopwords(tweet['text'])
                }
            )
        else:
            sentenceList = []
            if mode == 'nltk':
                sentenceList = nltkSentenceSplit(tweet['text'])
            elif mode == 'regex':
                sentenceList = regexSentenceSplit(tweet['text'])

            for i in range(0,len(sentenceList)):
                sentenceList[i] = remove_stopwords(sentenceList[i])

            outTweetList.append(
                {
                    'text': tweet['text'],
                    'date': tweet['date'],
                    'cleanedSentences': sentenceList
                }
            )

    f = open(outputJson, "w")
    f.write(json.dumps(outTweetList))
    f.close()

    print(outputJson)
