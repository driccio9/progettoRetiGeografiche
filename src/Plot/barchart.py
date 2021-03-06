import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def barchartText2Emotion(inputJsonList, labels, title, outputFile='none', show=False):

    sentimentMeanList = []

    for i in range(0, len(inputJsonList)):
        #recupero per ogni partito politico il vettore della media dei sentimenti
        sentimentMean = pd.read_json(inputJsonList[i],  convert_dates=False)[['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)

        #normalizzo il vettore
        sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)

        sentimentMeanList.append(sentimentMean*100)

    sentimentMeanMatrix = np.array(sentimentMeanList)
    cumSum = sentimentMeanMatrix.cumsum(axis=1)

    fig = plt.subplots(figsize=(10, 7))
    plt.grid(color='green', linestyle='--', linewidth=0.5, axis='y')

    ind = np.arange(len(labels))
    width = 0.35

    # list of bar
    barList = []
    # list of rec
    rectList = []

    barList.append(plt.bar(ind, sentimentMeanMatrix[:, 0], width))
    rectList.append(barList[0][0])

    for i in range(1, sentimentMeanMatrix.shape[1]):
        barList.append(plt.bar(ind, sentimentMeanMatrix[:, i], width, bottom=cumSum[:, i - 1]))
        rectList.append(barList[i][0])

    plt.ylabel('sentiment %')
    plt.title(title)
    plt.xticks(ind, labels)
    plt.yticks(np.arange(0, 105, 5))

    plt.legend(rectList, ('happy', 'angry', 'surprise', 'sad', 'fear'))

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def barchartVader(inputJsonList, labels, title, outputFile='none', show=False):

    sentimentMeanList = []
    for i in range(0, len(inputJsonList)):

        #recupero per ogni partito politico il vettore della media dei sentimenti
        sentimentMean = pd.read_json(inputJsonList[i],  convert_dates=False)[['negative', 'neutral', 'positive']].mean(axis=0)

        sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)

        sentimentMeanList.append(sentimentMean*100)

    sentimentMeanMatrix = np.array(sentimentMeanList)
    cumSum = sentimentMeanMatrix.cumsum(axis=1)

    fig = plt.subplots(figsize=(10, 7))
    plt.grid(color='green', linestyle='--', linewidth=0.5, axis='y')

    ind = np.arange(len(labels))
    width = 0.35

    # list of bar
    barList = []
    # list of rec
    rectList = []

    barList.append(plt.bar(ind, sentimentMeanMatrix[:, 0], width))
    rectList.append(barList[0][0])

    for i in range(1, sentimentMeanMatrix.shape[1]):
        barList.append(plt.bar(ind, sentimentMeanMatrix[:, i], width, bottom=cumSum[:, i - 1]))
        rectList.append(barList[i][0])

    plt.ylabel('sentiment %')
    plt.title(title)
    plt.xticks(ind, labels)
    plt.yticks(np.arange(0, 105, 5))

    plt.legend(rectList, ('negative', 'neutral', 'positive'))

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def barchartTextBlob(inputJsonList, labels, title, outputFile='none', show=False):

    sentimentMeanList = []

    for i in range(0, len(inputJsonList)):

        df = pd.read_json(inputJsonList[i],  convert_dates=False)

        sentimentMeanList.append(
            [
                (df[df['polarity'] < 0].shape[0] / df.shape[0]) * 100,
                (df[df['polarity'] == 0].shape[0] / df.shape[0]) * 100,
                (df[df['polarity'] > 0].shape[0] / df.shape[0]) * 100
            ]
        )

    sentimentMeanMatrix = np.array(sentimentMeanList)
    cumSum = sentimentMeanMatrix.cumsum(axis=1)

    fig = plt.subplots(figsize=(10, 7))
    plt.grid(color='green', linestyle='--', linewidth=0.5, axis='y')

    ind = np.arange(len(labels))
    width = 0.35

    #list of bar
    barList = []
    #list of rec
    rectList = []

    barList.append(plt.bar(ind, sentimentMeanMatrix[:, 0], width))
    rectList.append(barList[0][0])


    for i in range(1, sentimentMeanMatrix.shape[1]):
        barList.append(plt.bar(ind, sentimentMeanMatrix[:, i], width, bottom=cumSum[:, i-1]))
        rectList.append(barList[i][0])

    plt.ylabel('sentiment %')
    plt.title(title)
    plt.xticks(ind, labels)
    plt.yticks(np.arange(0, 105, 5))

    plt.legend(rectList, ('negative', 'neutral', 'positive'))

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def barchartComparesDates(inputJson, modeAnalysisTool, dates, title, outputFile='none', show=False):
    valid = {'vader', 't2e', 'tb'}
    if modeAnalysisTool not in valid:
        raise ValueError('mode must be one of %r.' % valid)

    df = pd.read_json(inputJson, convert_dates=False)

    sentimentMeanList = []
    for date in dates:
        if modeAnalysisTool == 'vader':
            sentimentMean = df[df['date'] == date][['negative', 'neutral', 'positive']].mean(axis=0)
            sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)
            sentimentMeanList.append(sentimentMean * 100)
        elif modeAnalysisTool == 't2e':
            sentimentMean = df[df['date'] == date][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)
            sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)
            sentimentMeanList.append(sentimentMean * 100)
        elif modeAnalysisTool == 'tb':
            sentimentMeanList.append(
                [
                    (df[df['date'] == date][df['polarity'] < 0].shape[0] / df[df['date'] == date].shape[0]) * 100,
                    (df[df['date'] == date][df['polarity'] == 0].shape[0] / df[df['date'] == date].shape[0]) * 100,
                    (df[df['date'] == date][df['polarity'] > 0].shape[0] / df[df['date'] == date].shape[0]) * 100
                ]
            )

    sentimentMeanMatrix = np.array(sentimentMeanList)
    cumSum = sentimentMeanMatrix.cumsum(axis=1)

    fig = plt.subplots(figsize=(10, 7))
    plt.grid(color='green', linestyle='--', linewidth=0.5, axis='y')

    ind = np.arange(len(dates))
    width = 0.35

    # list of bar
    barList = []
    # list of rec
    rectList = []

    barList.append(plt.bar(ind, sentimentMeanMatrix[:, 0], width))
    rectList.append(barList[0][0])

    for i in range(1, sentimentMeanMatrix.shape[1]):
        barList.append(plt.bar(ind, sentimentMeanMatrix[:, i], width, bottom=cumSum[:, i - 1]))
        rectList.append(barList[i][0])

    plt.ylabel('sentiment %')
    plt.title(title)
    plt.xticks(ind, dates)
    plt.yticks(np.arange(0, 105, 5))

    if modeAnalysisTool == 't2e':
        plt.legend(rectList, ('happy', 'angry', 'surprise', 'sad', 'fear'))
    else:
        plt.legend(rectList, ('negative', 'neutral', 'positive'))


    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()