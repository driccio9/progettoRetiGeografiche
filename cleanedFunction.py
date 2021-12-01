import re

x = 'RT @fausername1: @fakeusername2 just bought 30.6 BTC from https://fakeesceafafa.com &amp; I am hating the crash\n Hope it recovers so... '
#rimozione ...
x = re.sub("\\.\\.\\.", '', x)
print(x)
#parseHTML chars

# import html
import html
x = html.unescape(x)
print(x)

#remove hyperlinks
x = re.sub("http\S+", '', x)
print(x)

#remove numbers
x = re.sub("([+-]?[0-9]+)|([-+]?[0-9]*.[0-9]+)", '', x)
print(x)

#remove mentions, hashtags and retweet tags
