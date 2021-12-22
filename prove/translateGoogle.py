import pandas as pd
from googletrans import Translator
from cleanedFunction import cleaned, remove_stopwords

def translateByPoliticalParty():
    words = [
        '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)',
        '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)',
        '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)',
        '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)',
        '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)',
        '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)',
        '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)'
    ]

    translator = Translator()

    for word in words:
        word = word + '.json'
        print('processing ' + word)
        df = pd.read_json('..\\' + word,  convert_dates=False)
        df.drop_duplicates(subset=['text', 'date'], keep='first', inplace=True)

        print('cleaning...')
        df['text'] = df['text'].map(cleaned)

        try:
            df['text'] = df['text'].map(lambda x: translator.translate(x, dest='en', src='it').text)
        finally:
            print('removing sw...')
            df['text'] = df['text'].map(remove_stopwords)

            print('saving...')
            df.drop_duplicates(subset=['text', 'date'], keep='first', inplace=True)
            df.to_json('..\\sample\\TRANSLATED_' + word, orient='records')
            print('saved!\n')


def translateAllTweet():
    input = r'..\alltweet.json'
    output = r'..\sample\TRANSLATED_alltweet.json'

    df = pd.read_json(input, convert_dates=False)

    df.drop_duplicates(subset=['text', 'date'], keep='first', inplace=True)

    translator = Translator()

    try:
        print('transleting...')
        df['text'] = df['text'].map(lambda x: translator.translate(x, dest='en', src='it').text)
    finally:
        print('removing sw...')
        df['text'] = df['text'].map(remove_stopwords)

        df.drop_duplicates(subset=['text', 'date'], keep='first', inplace=True)
        print('saving...')
        df.to_json(output, orient='records')
