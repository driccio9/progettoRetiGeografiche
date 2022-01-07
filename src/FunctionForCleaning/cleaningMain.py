from cleanedFunction import preProcessing

dirInput ="../TranslatedTweet/"
dirOutput = "../CleanedTweet/"

modeList = ["none", "nltk", "regex"]

postfix = ".json"

#per questioni di prove manca l'hashtag #greenpass. Attenzione!
words = [
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
    "(#greenpass OR #supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
]


for mode in modeList:

    #per i partiti
    for word in words:
        preProcessing(
            inputJson=dirInput + word + postfix,
            outputJson=dirOutput + mode + "_" + word + postfix,
            mode=mode
        )

    #per all tweet
    preProcessing(
        inputJson=dirInput + "allTweetTranslate" + postfix,
        outputJson=dirOutput + mode + "_" + "allTweet" + postfix,
        mode=mode
    )


