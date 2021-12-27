import pandas as pd
import matplotlib.pyplot as plt


def pieChartText2Emotion(inputJson, title, outputFile='none', show=False):
    dataFrame = pd.read_json(inputJson, convert_dates=False)
    mean = dataFrame[['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)
    labels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    patches, texts, junk = plt.pie(mean.values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def pieChartVader(inputJson, title, outputFile='none', show=False):
    dataFrame = pd.read_json(inputJson, convert_dates=False)
    mean = dataFrame[['negative', 'positive', 'neutral']].mean(axis=0)
    labels = ['negative', 'positive', 'neutral']
    patches, texts, junk = plt.pie(mean.values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def pieChartTextBlob(inputJson, title, outputFile='none', show=False):
    df = pd.read_json(inputJson, convert_dates=False)

    positive = (df[df['polarity'] > 0].shape[0] / df.shape[0]) * 100
    neutral = (df[df['polarity'] == 0].shape[0] / df.shape[0]) * 100
    negative = (df[df['polarity'] < 0].shape[0] / df.shape[0]) * 100

    values = [positive, neutral, negative]
    labels = ['positive', 'neutral', 'negative']
    patches, texts, junk = plt.pie(values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def pieChartTextBlobByDate(date, inputJson, title, outputFile='none', show=False):
    df = pd.read_json(inputJson, convert_dates=False)
    df = df[df['date'].str.contains(date)]

    positive = (df[df['polarity'] > 0].shape[0] / df.shape[0]) * 100
    neutral = (df[df['polarity'] == 0].shape[0] / df.shape[0]) * 100
    negative = (df[df['polarity'] < 0].shape[0] / df.shape[0]) * 100

    values = [positive, neutral, negative]
    labels = ['positive', 'neutral', 'negative']
    patches, texts, junk = plt.pie(values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def pieChartVaderByDate(date, inputJson, title, outputFile='none', show=False):
    dataFrame = pd.read_json(inputJson, convert_dates=False)
    dataFrame = dataFrame[dataFrame['date'].str.contains(date)]
    mean = dataFrame[['negative', 'positive', 'neutral']].mean(axis=0)
    labels = ['negative', 'positive', 'neutral']
    patches, texts, junk = plt.pie(mean.values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def pieChartText2EmotionByDate(date, inputJson, title, outputFile='none', show=False):
    dataFrame = pd.read_json(inputJson, convert_dates=False)
    dataFrame = dataFrame[dataFrame['date'].str.contains(date)]
    mean = dataFrame[['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)
    labels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    patches, texts, junk = plt.pie(mean.values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()
