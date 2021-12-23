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


def funchartVader(jsonFile, title, outputFile='none', show=False):
    df = pd.read_json(jsonFile, convert_dates=False)
    days = df['date'].drop_duplicates(keep='first', inplace=False).values
    days.sort()
    sentimentMeanList = []
    for day in days:
        sentimentMean = df[df['date'] == day][['negative', 'positive', 'neutral']].mean(axis=0)
        #sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)
        sentimentMean *= 100
        sentimentMeanList.append(sentimentMean)

    sentimentMeanMatrix = np.array(sentimentMeanList)

    labels = ('negative', 'positive', 'neutral')

    for i in range(0, sentimentMeanMatrix.shape[1]):
        plt.plot(days, sentimentMeanMatrix[:, i], label=labels[i])

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


def funchartTextBlob(jsonFile, title, outputFile='none', show=False):
    df = pd.read_json(jsonFile, convert_dates=False)

    dayList = df['date'].drop_duplicates(keep='first', inplace=False).values
    dayList.sort()
    polarityMeanList = []
    for day in dayList:
        polarityMeanList.append(float(df[df['date'] == day]['polarity'].mean(axis=0)))

    plt.plot(dayList, polarityMeanList, label=('polarity'))

    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.yticks(np.arange(-1, 1, 0.10))
    plt.grid()
    plt.xlabel('day')
    plt.ylabel('sentiment mean')
    plt.title(title)
    plt.legend()

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()

