import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def funchartT2E(jsonFile, title, outputFile='none', show=False):
    df = pd.read_json(jsonFile, convert_dates=False)
    days = df['date'].drop_duplicates(keep='first', inplace=False).values
    days.sort()
    sentimentMeanList = []
    for day in days:
        sentimentMean = df[df['date'] == day][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)
        sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)
        sentimentMean *= 100
        sentimentMeanList.append(sentimentMean)

    sentimentMeanMatrix = np.array(sentimentMeanList)

    labels = ('Happy', 'Angry', 'Surprise', 'Sad', 'Fear')



    for i in range(0, sentimentMeanMatrix.shape[1]):
        plt.plot(days, sentimentMeanMatrix[:,i], label=labels[i])

    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.yticks(np.arange(0, 100, 5))

    plt.xlabel('day')
    plt.ylabel('sentiment mean')
    plt.title(title)
    plt.legend()

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def funchartVader(inputJsonList, labels, title, outputFile='none', show=False):

    fig = plt.subplots(figsize=(10, 7))
    # nel caso si abbia un unico file, stampo la variazione dei 3 sentimenti nel tempo
    if len(inputJsonList) == 1:
        df = pd.read_json(inputJsonList[0], convert_dates=False)
        days = df['date'].drop_duplicates(keep='first', inplace=False).values
        days.sort()
        sentimentMeanList = []
        for day in days:
            sentimentMean = df[df['date'] == day][['negative', 'neutral', 'positive']].mean(axis=0)
            sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)
            sentimentMean *= 100
            sentimentMeanList.append(sentimentMean)

        sentimentMeanMatrix = np.array(sentimentMeanList)

        sentiments = ('negative', 'neutral', 'positive')

        for i in range(0, sentimentMeanMatrix.shape[1]):
            plt.plot(days, sentimentMeanMatrix[:, i], label=sentiments[i])

    # altrimenti confronta tutti i file sul valore di compound nel tempo
    else:
        for i in range(0, len(inputJsonList)):
            df = pd.read_json(inputJsonList[i], convert_dates=False)
            dayList = df['date'].drop_duplicates(keep='first', inplace=False).values
            dayList.sort()
            polarityMeanList = []
            for day in dayList:
                polarityMeanList.append(float(df[df['date'] == day]['compound'].mean(axis=0)))

            plt.plot(dayList, polarityMeanList, label=labels[i])


    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)

    if len(inputJsonList) == 1:
        plt.yticks(np.arange(0, 100, 5))
        plt.ylabel('sentiment mean')
    else:
        plt.yticks(np.arange(-1, 1, 0.10))
        plt.ylabel('compound')

    plt.grid()
    plt.xlabel('day')

    plt.title(title)
    plt.legend()

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def funchartTextBlob(inputJsonList, labels, title, outputFile='none', show=False):
    fig = plt.subplots(figsize=(10, 7))
    for i in range(0, len(inputJsonList)):
        df = pd.read_json(inputJsonList[i], convert_dates=False)
        dayList = df['date'].drop_duplicates(keep='first', inplace=False).values
        dayList.sort()
        polarityMeanList = []
        for day in dayList:
            polarityMeanList.append(float(df[df['date'] == day]['polarity'].mean(axis=0)))

        plt.plot(dayList, polarityMeanList, label=labels[i])

    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.yticks(np.arange(-1, 1, 0.10))
    plt.grid()
    plt.xlabel('day')
    plt.ylabel('polarity')
    plt.title(title)
    plt.legend()

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def funchartVaderTextBlob(inputVader, inputTextBlob, title, outputFile='none', show=False):
    fig = plt.subplots(figsize=(10, 7))
    dfVader = pd.read_json(inputVader, convert_dates=False)
    dayListVader = dfVader['date'].drop_duplicates(keep='first', inplace=False).values
    dayListVader.sort()
    polarityMeanList = []
    for day in dayListVader:
        polarityMeanList.append(float(dfVader[dfVader['date'] == day]['compound'].mean(axis=0)))
    plt.plot(dayListVader, polarityMeanList, label="Vader_compound")

    dfTextBlob = pd.read_json(inputTextBlob, convert_dates=False)
    dayListTextBlob = dfTextBlob['date'].drop_duplicates(keep='first', inplace=False).values
    dayListTextBlob.sort()
    polarityMeanList = []
    for day in dayListTextBlob:
        polarityMeanList.append(float(dfTextBlob[dfTextBlob['date'] == day]['polarity'].mean(axis=0)))
    plt.plot(dayListTextBlob, polarityMeanList, label="TB_polarity")

    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.yticks(np.arange(-1, 1, 0.10))
    plt.grid()
    plt.xlabel('day')
    plt.ylabel('polarity/compound')
    plt.title(title)
    plt.legend()

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()
    pass