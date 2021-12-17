import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def barchartText2Emotion():
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

    dfList = []

    for i in range(0, len(words)):
        words[i] = prefix + words[i] + postfix
        dfList.append(pd.read_json(words[i],  convert_dates=False))
        print(dfList[i])

    meanMatrix = np.array(
        [
            dfList[0][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0).values*100,
            dfList[1][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0).values*100,
            dfList[2][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0).values*100,
            dfList[3][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0).values*100,
            dfList[4][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0).values*100,
            dfList[5][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0).values*100,
            dfList[6][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0).values*100
        ]
    )
    print(meanMatrix)

    meanMatrix = meanMatrix.transpose()
    print(meanMatrix)
    cumSum = meanMatrix.cumsum(axis=0)
    print(cumSum)

    N = 7
    ind = np.arange(N)
    print(ind)
    width = 0.35
    print(meanMatrix[0])

    fig = plt.subplots(figsize=(10, 7))
    p1 = plt.bar(ind, meanMatrix[0], width)
    p2 = plt.bar(ind, meanMatrix[1], width, bottom=cumSum[0])
    p3 = plt.bar(ind, meanMatrix[2], width, bottom=cumSum[1])
    p4 = plt.bar(ind, meanMatrix[3], width, bottom=cumSum[2])
    p5 = plt.bar(ind, meanMatrix[4], width, bottom=cumSum[3])

    plt.ylabel('emotions %')
    plt.title('emotions by political party')
    plt.xticks(ind, labels)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('happy', 'angry', 'surprise', 'sad', 'fear'))

    plt.show()

barchartText2Emotion()