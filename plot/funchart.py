import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def funchartT2E(jsonFile, title='sentiment day by day'):
    df = pd.read_json(jsonFile, convert_dates=False)
    days = df['date'].drop_duplicates(keep='first', inplace=False).values

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
    plt.show()


def funchartVader(jsonFile, title='sentiment day by day'):
    df = pd.read_json(jsonFile, convert_dates=False)
    days = df['date'].drop_duplicates(keep='first', inplace=False).values

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
    plt.show()

