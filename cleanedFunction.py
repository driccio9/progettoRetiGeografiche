import re
import html
import deepl
import nltk

#nltk.download('punkt')
#nltk.download('stopwords')
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
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words('italian')]
    return collapse_list_to_string(tokens_without_sw)


def translate(text: str):
    # Usare con cautela
    auth_key = "2f684879-0068-c95b-5523-aac8599ad960:fx"
    translator = deepl.Translator(auth_key)
    target_language = "EN-GB"
    result = translator.translate_text(text, target_lang=target_language)
    return result.text


def regexSentTokenize(text: str):
    return re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

def nltkSentTokenize(text : str):
    return nltk.sent_tokenize(text)

def removeRedundance(l: list):
        return [dict(t) for t in {tuple(d.items()) for d in l}]





