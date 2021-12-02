import pandas as pd
import nltk
import typing

def get_sentiment(text: str, analyser, desired_type: str = 'pos'):
    # Get sentiment from text
    sentiment_score = analyser.polarity_scores(text)
    return sentiment_score[desired_type]


# Get Sentiment scores
def get_sentiment_scores(df, data_column):
    df[f'{data_column} Positive Sentiment Score'] = df[data_column].astype(str).apply(
        lambda x: get_sentiment(x, sid_analyzer, 'pos'))
    df[f'{data_column} Negative Sentiment Score'] = df[data_column].astype(str).apply(
        lambda x: get_sentiment(x, sid_analyzer, 'neg'))
    df[f'{data_column} Neutral Sentiment Score'] = df[data_column].astype(str).apply(
        lambda x: get_sentiment(x, sid_analyzer, 'neu'))
    df[f'{data_column} Compound Sentiment Score'] = df[data_column].astype(str).apply(
        lambda x: get_sentiment(x, sid_analyzer, 'compound'))
    return df


def remove_links(text):
    # Remove any hyperlinks that may be in the text starting with http
    import re
    return re.sub(r"http\S+", "", text)

def style_text(text:str):
    # Convert to lowercase
    return text.lower()



def collapse_list_to_string(string_list):
    # This is to join back together the text data into a single string
    return ' '.join(string_list)

def remove_apostrophes(text):
    # Remove any apostrophes as these are irrelavent in our word cloud
    text = text.replace("'", "")
    text = text.replace('"', "")
    text = text.replace('`', "")
    return text




text = "RT @fausername1: @fakeusername2 just bought 30.6 BTC from https://fakeesceafafa.com &amp; I am hating the crah "


print(collapse_list_to_string(remove_words(text)))

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sid_analyzer = SentimentIntensityAnalyzer()
