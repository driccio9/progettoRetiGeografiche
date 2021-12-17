import pandas as pd
import matplotlib.pyplot as plt


def pieChartText2Emotion(dataFrame : pd.DataFrame):
    mean = dataFrame[['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)
    values = mean.values
    print(values)

    labels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    patches, texts, junk = plt.pie(values, labels=labels,  startangle=90, autopct='%.2f')
    plt.style.use('default')
    plt.title("Text to Emotion Result")
    plt.axis('equal')
    plt.show()

#Prova#########
df = pd.read_json(r'..\sample\text2emotionAllTweet.json', date_unit='s')
pieChartText2Emotion(df)
###############