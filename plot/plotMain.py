from barchart import *
from funchart import *

dirInput ="SentimentAnalysisToolsOutput/" #"../Tweet/"
dirOutput = "img/"

prefixList = ["T2E_", "TB_", "VADER_"]
modeList = ["none", "nltk", "regex"]
barchartFunList = [barchartText2Emotion, barchartTextBlob, barchartVader]
funchartFunList = [funchartT2E, funchartTextBlob, funchartVader]

postfixInput = ".json"
postfixOutput = ".png"

#per questioni di prove manca l'hashtag #greenpass. Attenzione!
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

for analysisToolIndex in range(0,len(barchartFunList)):
    for modeIndex in range(0, len(modeList)):

        inputJsonList = []
        for word in words:
            inputJsonList.append(dirInput + prefixList[analysisToolIndex] + modeList[modeIndex] + '_' + word + postfixInput)

        barchartFunList[analysisToolIndex](
            inputJsonList,
            labels,
            prefixList[analysisToolIndex] + modeList[modeIndex],
            dirOutput + 'barchart_' +prefixList[analysisToolIndex] + modeList[modeIndex]
        )


for analysisToolIndex in range(1,len(funchartFunList)):
    for modeIndex in range(0, len(modeList)):

        inputJsonList = []
        for word in words:
            inputJsonList.append(dirInput + prefixList[analysisToolIndex] + modeList[modeIndex] + '_' + word + postfixInput)

        funchartFunList[analysisToolIndex](
            inputJsonList,
            labels,
            prefixList[analysisToolIndex] + modeList[modeIndex],
            dirOutput + 'funchart_' +prefixList[analysisToolIndex] + modeList[modeIndex]
        )
