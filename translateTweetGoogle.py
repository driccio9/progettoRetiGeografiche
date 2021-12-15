import pandas as pd
from googletrans import Translator

input = "alltweet.json"
import json

all_tweet = []
f = open(input, "r")
all_tweet = json.loads(f.read())
f.close()

# carica il file json e rimuove i duplicati
i = 1000
j = 0
while i <= range(len(all_tweet)):
    df = pd.read_json(r'alltweet.json', date_unit='s')[j:i]

    df.drop_duplicates(subset=['text', 'date'], keep='first', inplace=True)

    translator = Translator()

    print("traduco...")

    results = translator.translate(df['text'].values.tolist(), dest='en', src='it')
    df['text'] = pd.DataFrame(results)
    df['text'] = df.text.map(lambda x: x.text)

    df.to_json('translatedAllTweet.json', orient='records')
    #vedere come redendere il to json in append mode (quindi senza cancellare il precedente contenuto)
    j = i
    i += 1000


""" 
#rimuove i duplicati
df.drop_duplicates(subset='text', keep='first', inplace=True)

df.rename(columns={'text': 'originalText'}, inplace=True)

df['cleanedItalianText'] = df.originalText.map(cleaned)

df['cleanedEnglishText'] = df.cleanedItalianText.map(translate).map(remove_stopwords)

df.to_json('sample.json', orient='records')
"""
