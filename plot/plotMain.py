from barchart import *
from funchart import *
from densitychart import *
from piechart import *

dirInput ="SentimentAnalysisToolsOutput/" #"../Tweet/"
dirOutput = "img/"


toolList = ["T2E", "TB", "VADER"]
modeList = ["none", "nltk", "regex"]
barchartFunList = [barchartText2Emotion, barchartTextBlob, barchartVader]
funchartFunList = [funchartT2E, funchartTextBlob, funchartVader]
densitychartFunList = [None, densitychartTextBlob, densitychartVader]
pieChart = []


postfixInput = ".json"

#per questioni di prove manca l'hashtag #greenpass. Attenzione!
words = [
    '(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)',
    '(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)',
    '(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)',
    '(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)',
    '(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)',
    '(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)',
    '(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)'
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

"""
for analysisToolIndex in range(0, len(barchartFunList)):
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


for analysisToolIndex in range(1, len(funchartFunList)):
    for modeIndex in range(0, len(modeList)):

        inputJsonList = []
        for word in words:
            inputJsonList.append(dirInput + toolList[analysisToolIndex] + '_' + modeList[modeIndex] + '_' + word + postfixInput)

        funchartFunList[analysisToolIndex](
            inputJsonList,
            labels,
            toolList[analysisToolIndex] + '_' + modeList[modeIndex],
            dirOutput + 'funchart_' + toolList[analysisToolIndex] + '_' + modeList[modeIndex]
        )


#plotting density chart

#attenzione da cambiare con alltweet quando sarà processato dai tools di sentiment analysis
alltweetfilename = 'allTweet'

for analysisToolIndex in range(1, len(densitychartFunList)):
    inputJsonList = []
    for modeIndex in range(0, len(modeList)):
        inputJsonList.append(dirInput + toolList[analysisToolIndex] + '_' + modeList[modeIndex] + '_' + alltweetfilename + postfixInput)

    print(inputJsonList)
    densitychartFunList[analysisToolIndex](
        inputJsonList,
        modeList,
        "comparison between pdfs on preprocessing paths with " + toolList[analysisToolIndex],
        dirOutput + 'densitychart_' + toolList[analysisToolIndex] + '_'
    )
"""

for politicalIndex in range(0, len(words)):
    for toolIndex in range(0, len(toolList)):

        inputJsonList = []
        for modeIndex in range(0, len(modeList)):
            inputJsonList.append(
                dirInput + toolList[toolIndex] + '_' + modeList[modeIndex] + '_' + words[politicalIndex] + postfixInput
            )

        print(inputJsonList)
        if toolList[toolIndex] == 'T2E':
            barchartText2Emotion(
                inputJsonList=inputJsonList,
                labels=modeList,
                title=toolList[toolIndex] + '_' + labels[politicalIndex],
                outputFile=dirOutput + 'barchart_T2E_' + labels[politicalIndex]
            )
        elif toolList[toolIndex] == 'TB':
            funchartTextBlob(
                inputJsonList=inputJsonList,
                labels=modeList,
                title=toolList[toolIndex] + '_' + labels[politicalIndex],
                outputFile=dirOutput + 'funchart_TB_' + labels[politicalIndex]
            )
        elif toolList[toolIndex] == 'VADER':
            funchartVader(
                inputJsonList=inputJsonList,
                labels=modeList,
                title=toolList[toolIndex] + '_' + labels[politicalIndex],
                outputFile=dirOutput + 'funchart_VADER_' + labels[politicalIndex]
            )


pieChartVader(
    'SentimentAnalysisToolsOutput/VADER_none_(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega).json',
    'prova',
    show=True
)