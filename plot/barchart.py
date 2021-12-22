import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def barchartText2Emotion(title='emotions by political party'):
    prefix = r"..\sample\T2E_"
    postfix = ".json"
    words = [
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
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

    sentimentMeanList = []

    for i in range(0, len(words)):
        words[i] = prefix + words[i] + postfix

        #recupero per ogni partito politico il vettore della media dei sentimenti
        sentimentMean = pd.read_json(words[i],  convert_dates=False)[['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)

        #normalizzo il vettore
        sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)

        sentimentMeanList.append(sentimentMean*100)


    sentimentMeanMatrix = np.array(sentimentMeanList)

    fig = plt.subplots(figsize=(10, 7))
    plt.grid(color='green', linestyle='--', linewidth=0.5, axis='y')

    ind = np.arange(7)
    width = 0.35
    p = []
    cumSum = sentimentMeanMatrix.cumsum(axis=1)
    p.append(plt.bar(ind, sentimentMeanMatrix[:, 0], width))

    for i in range(1, sentimentMeanMatrix.shape[1]):
        p.append(plt.bar(ind, sentimentMeanMatrix[:, i], width, bottom=cumSum[:, i-1]))

    plt.ylabel('emotions %')
    plt.title(title)
    plt.xticks(ind, labels)
    plt.yticks(np.arange(0, 105, 5))

    plt.legend((p[0][0], p[1][0], p[2][0], p[3][0], p[4][0]), ('happy', 'angry', 'surprise', 'sad', 'fear'))
    plt.show()


def barchartVader(title='emotions by political party'):
    prefix = r"..\sample\VADER_"
    postfix = ".json"
    words = [
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (meloni OR fdi OR fratellidiitalia)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (m5s OR dimaio OR conte OR maio)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (renzi OR italiaviva)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (berlusconi OR forzaitalia)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (bersani OR articolouno)",
        "(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (letta OR pd)"
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

    sentimentMeanList = []

    for i in range(0, len(words)):
        words[i] = prefix + words[i] + postfix

        #recupero per ogni partito politico il vettore della media dei sentimenti
        sentimentMean = pd.read_json(words[i],  convert_dates=False)[['negative', 'positive', 'neutral']].mean(axis=0)

        #sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)

        sentimentMeanList.append(sentimentMean*100)


    sentimentMeanMatrix = np.array(sentimentMeanList)

    fig = plt.subplots(figsize=(10, 7))
    plt.grid(color='green', linestyle='--', linewidth=0.5, axis='y')

    ind = np.arange(7)
    width = 0.35

    #list of bar
    p = []

    cumSum = sentimentMeanMatrix.cumsum(axis=1)
    p.append(plt.bar(ind, sentimentMeanMatrix[:, 0], width))

    for i in range(1, sentimentMeanMatrix.shape[1]):
        p.append(plt.bar(ind, sentimentMeanMatrix[:, i], width, bottom=cumSum[:, i-1]))

    plt.ylabel('sentiment %')
    plt.title(title)
    plt.xticks(ind, labels)
    plt.yticks(np.arange(0, 105, 5))

    plt.legend((p[0][0], p[1][0], p[2][0]), ('negative', 'positive', 'neutral'))
    plt.show()
