import re
import html

x = 'RT @fausername1: @fakeusername2 just bought 30.6 BTC from https://fakeesceafafa.com &amp; I am hating the crash\n Hope it recovers so... '

def cleaned(text):
    text = re.sub(
        "(#\S+)|(RT @\w+:)|(@\S+)|([+-]?[0-9]+)|([-+]?[0-9]*.[0-9]+)|(http\S+)|(\.\.\.)",
        '',
        html.unescape(text)
    )
    return text.lower()

print(cleaned(x))