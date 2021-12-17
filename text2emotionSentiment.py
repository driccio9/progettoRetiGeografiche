import text2emotion as te
import pandas as pd

#il testo deve essere tradotto in linugua inglese
def text2emotion(dataFrame:pd.DataFrame, outPathFile):
    emotions = dataFrame['text'].map(te.get_emotion).tolist()
    dataFrame = pd.concat([dataFrame, pd.DataFrame(emotions)], axis=1)
    dataFrame.to_json(outPathFile, orient='records')

"""
#Prova#########
df = pd.read_json(r'alltweet.json',  convert_dates=False)
text2emotion(df, r'sample/text2emotionAllTweet.json')
################
"""

prefix = r'sample\TRANSLATED_'
postfix = '.json'
outPrefix = r'sample\T2E_'

words = [
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)'
]

for i in range(0,len(words)):
    df = pd.read_json(prefix+words[i]+postfix, convert_dates=False)
    text2emotion(df, outPrefix+words[i]+postfix)


