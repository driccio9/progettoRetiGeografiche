from SentimentAnalysisTools.text2emotionSentiment import *
from SentimentAnalysisTools.textBlobSentiment import *
from SentimentAnalysisTools.vaderSentiment import *

dirInput ="sample/" #"../Tweet/"
dirOutput = "SentimentAnalysisToolsOutput/"

prefixInput = "TRANSLATED_"

prefixOutput = ["T2E_", "TB_", "VADER_"]
mode = ["none", "nltk", "regex"]
analysisTools = [text2emotionSentiment, textBlobSentiment, vaderSentiment]

postfix = ".json"
#WIP...

#per questioni di prove manca l'hashtag #greenpass. Attenzione!
words = [
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
    "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
]

for analysisToolsIndex in range(0, len(analysisTools)):
    for modeIndex in range(0, len(mode)):
        for word in words:
            inputJson = dirInput + prefixInput + word + postfix
            outputJson = dirOutput + prefixOutput[analysisToolsIndex] + mode[modeIndex] + "_" + word + postfix
            print(inputJson)
            print(outputJson)
            analysisTools[analysisToolsIndex](inputJson, outputJson, mode[modeIndex])









