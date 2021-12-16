import time
import pandas as pd
from googletrans import Translator

input = "alltweet.json"
output = "translatedAllTweet.json"

df = pd.read_json(r'alltweet.json', date_unit='s')
df.drop_duplicates(subset=['text', 'date'], keep='first', inplace=True)

translator = Translator()

try:
    df['text'] = df['text'].map(lambda x: translator.translate(x, dest='en', src='it').text)
finally:
    df.to_json(output, orient='records')


df['cleanedItalianText'] = df.originalText.map(cleaned)

df['cleanedEnglishText'] = df.cleanedItalianText.map(translate).map(remove_stopwords)

df.to_json('sample.json', orient='records')
"""
