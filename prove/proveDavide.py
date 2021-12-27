from googletrans import Translator
import numpy as np
import json
import text2emotion as te
import pandas as pd
from plot.piechart import *
from SentimentAnalysisTools.textBlobSentiment import *
from SentimentAnalysisTools.vaderSentiment import *
from plot.funchart import *
from plot.barchart import *
from FunctionForCleaning.cleanedFunction import *
from plot.densitychart import *

#x = 'RT @fausername1: @fakeusername2 just bought 30.6 BTC from https://fakeesceafafa.com &amp; I am hating the crash\n Hope it recovers so... '
x = '''RT @Morrison: ATAGI says we must have boosters 5mths after our 2nd vax, I'll follow their advice, they're the experts.
Also Morrison @fakeusername2: Even though ATAGI wants mask mandates I won't follow their advice bcuz I don't like it, that one comes down to individual responsibility.
Honeybee
#auspol"'''

words = [
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)',
    '(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)'
]

labels = (
    "Lega",
    "FDI",
    "M5S",
    "IV",
    "FI",
    "A1",
    "PD"
)

prefix = 'sample/VADER_'
postfix = '.json'
outPrefix = 'sample/'

"""

inputJsonList = []
inputLabel = []
for word in words:
    inputJsonList.append(prefix+word+postfix)

#funchartTextBlob(inputJsonList,labels,"polarity by political party",show=True)
funchartVader(inputJsonList,labels,"polarity by political party",show=True)
"""

inputJsonList = []
dirInput = 'SentimentAnalysisToolsOutput/'
prefixList = ['TB_nltk_', 'TB_regex_', 'TB_none_']
for i in range(0,len(prefixList)):
    inputJsonList.append(dirInput + prefixList[i] + words[0] + postfix)

print(inputJsonList)
densitychartTextBlob(inputJsonList, prefixList, 'densityTextBlob', show=True)
