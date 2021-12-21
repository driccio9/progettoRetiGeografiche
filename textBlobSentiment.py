from textblob import TextBlob
import json

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
input = "translate.json"

all_tweet = []
f = open(input, "r")
all_tweet = json.loads(f.read())
f.close()

i = 0

for sentence in all_tweet:
    print(sentence["text"])
    analysis = TextBlob(sentence["text"])
    print(analysis.sentiment)
    if analysis.sentiment[0] > 0:
        print('Positive')
    elif analysis.sentiment[0] < 0:
        print('Negative')
    else:
        print('Neutral')
    if i == 10:
        i += 1
        break
