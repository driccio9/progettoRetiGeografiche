import pandas as pd
import matplotlib.pyplot as plt
import json


def pieChartText2Emotion(inputJson, title="Text to Emotion Result"):
    dataFrame = pd.read_json(inputJson, convert_dates=False)
    mean = dataFrame[['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)
    labels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    patches, texts, junk = plt.pie(mean.values, labels=labels,  startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    plt.show()


def pieChartVader(inputJson, title="Vader"):
    dataFrame = pd.read_json(inputJson, convert_dates=False)
    mean = dataFrame[['negative', 'positive', 'neutral']].mean(axis=0)
    labels = ['negative', 'positive', 'neutral']
    patches, texts, junk = plt.pie(mean.values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    plt.show()


def pieChartTextBlob(inputJson, title="Text blob"):
    df = pd.read_json(inputJson, convert_dates=False)

    positive = (df[df['polarity'] > 0].shape[0]/df.shape[0])*100
    neutral = (df[df['polarity'] == 0].shape[0]/df.shape[0])*100
    negative = (df[df['polarity'] < 0].shape[0]/df.shape[0])*100

    values = [positive, neutral, negative]
    labels = ['positive', 'neutral', 'negative']
    patches, texts, junk = plt.pie(values, labels=labels, startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title(title)
    plt.axis('equal')
    plt.show()


