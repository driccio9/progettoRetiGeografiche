from src.SentimentAnalysisTools.text2emotionSentiment import *
from src.SentimentAnalysisTools.textBlobSentiment import *
from src.SentimentAnalysisTools.vaderSentiment import *
from threading import Thread


class MyThread(Thread):
    def __init__(self, tool, inputJson, outputJson, mode):
        Thread.__init__(self)
        self.tool = tool
        self.inputJson = inputJson
        self.outputJson = outputJson
        self.mode = mode

    def run(self):
        print("Thread '" + self.name + "' avviato")
        self.tool(self.inputJson, self.outputJson, self.mode)
        print("Thread '" + self.name + "' terminato")


numThreads = 4

dirInput = "data/CleanedTweet/"
dirOutput = "data/SentimentAnalysisToolsOutput/"

prefixOutput = ["T2E_", "TB_", "VADER_"]
mode = ["none", "nltk", "regex"]
analysisTools = [text2emotionSentiment, textBlobSentiment, vaderSentiment]
postfix = ".json"

# per questioni di prove manca l'hashtag #greenpass OR. Attenzione!
words = [
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
]

threadListAllTweet = []
threadListOtherTweet = []

for analysisToolsIndex in range(0, len(analysisTools)):
    for modeIndex in range(0, len(mode)):

        #per alltweet
        if analysisToolsIndex == 0: # se il tool è t2e procedo senza multithreading
            analysisTools[analysisToolsIndex](
                dirInput + mode[modeIndex] + "_" + "allTweet" + postfix,
                dirOutput + prefixOutput[analysisToolsIndex] + mode[modeIndex] + "_" + "allTweet" + postfix,
                mode[modeIndex]
            )
        else:
            threadListAllTweet.append(
                MyThread(
                    tool=analysisTools[analysisToolsIndex],
                    inputJson=dirInput + mode[modeIndex] + "_" + "allTweet" + postfix,
                    outputJson=dirOutput + prefixOutput[analysisToolsIndex] + mode[
                        modeIndex] + "_" + "allTweet" + postfix,
                    mode=mode[modeIndex]
                )
            )

        # per ogni partito
        for word in words:

            inputJson = dirInput + mode[modeIndex] + "_" + word + postfix
            outputJson = dirOutput + prefixOutput[analysisToolsIndex] + mode[modeIndex] + "_" + word + postfix

            # se il tool è t2e procedo senza multithreading
            if analysisToolsIndex == 0:
                analysisTools[analysisToolsIndex](inputJson, outputJson, mode[modeIndex])
            else:
                threadListOtherTweet.append(
                    MyThread(
                        tool=analysisTools[analysisToolsIndex],
                        inputJson=inputJson,
                        outputJson=outputJson,
                        mode=mode[modeIndex]
                    )
                )

joinIndex = 0
for i in range(0, len(threadListAllTweet)):

    threadListAllTweet[i].start()

    if (i+1) % numThreads == 0 or i == len(threadListAllTweet) - 1:
        while joinIndex <= i:
            threadListAllTweet[joinIndex].join()
            joinIndex += 1


joinIndex = 0
for i in range(0, len(threadListOtherTweet)):

    threadListOtherTweet[i].start()

    if (i + 1) % numThreads == 0 or i == len(threadListOtherTweet) - 1:
        while joinIndex <= i:
            threadListOtherTweet[joinIndex].join()
            joinIndex += 1
