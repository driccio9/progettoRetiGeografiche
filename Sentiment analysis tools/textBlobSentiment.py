import json

from textblob import TextBlob

from vaderSentiment import percentage

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
dir  = "../sample/"
inputfile = "TRANSLATED_(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia).json"
input = dir + inputfile
output = dir + "TB_" + inputfile

all_tweet = []
f = open(input, "r")
all_tweet = json.loads(f.read())
f.close()

i = 0

textblobresult = []
positive = 0
negative = 0
neutral = 0
polarity = 0
neutral_list = []
negative_list = []
positive_list = []
sentimet_tweet = []
noOfTweet = len(all_tweet)

print("processo")
for sentence in all_tweet:
    text = sentence["text"]
    analysis = TextBlob(text)
    textblobresult.append({'text': text, 'date': sentence["date"], 'polarity': analysis.sentiment[0],'subjectivity': analysis.sentiment[1]})
    if analysis.sentiment[0] > 0:
        positive_list.append(text)
        positive += 1
    elif analysis.sentiment[0] < 0:
        negative_list.append(text)
        negative += 1
    else:
        neutral_list.append(text)
        neutral += 1

positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

print("total number: ", noOfTweet)
print("positive number: ", len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ", len(neutral_list))

f = open(output, "w")
f.write(json.dumps(textblobresult))
f.close()
