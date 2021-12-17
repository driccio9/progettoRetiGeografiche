import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def funchartT2E(jsonFile):
    df = pd.read_json(jsonFile, convert_dates=False)
    days = df['date'].drop_duplicates(keep='first', inplace=False).values

    sentimentMeanList = []
    for day in days:
        sentimentMean = df[df['date'] == day][['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']].mean(axis=0)
        sentimentMean = sentimentMean / np.linalg.norm(sentimentMean, ord=1)
        sentimentMeanList.append(sentimentMean)

    sentimentMeanMatrix = np.array(sentimentMeanList)

    labels = ('Happy', 'Angry', 'Surprise', 'Sad', 'Fear')

    for i in range(0, sentimentMeanMatrix.shape[1]):
        plt.plot(days, sentimentMeanMatrix[:,i], label=labels[i])


    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.yticks(np.arange(0, 1, 0.05))

    # naming the x axis
    plt.xlabel('day')
    # naming the y axis
    plt.ylabel('sentiment mean')
    # giving a title to my graph
    plt.title('sentiment day by day')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


prefix = '..\\sample\\'
postfix = ''
input = r'T2E_(#supergreenpass OR #greenpassrafforzato OR #obbligovaccinale OR #vaccinoobbligatorio) (salvini OR lega).json'

funchartT2E(prefix+input+postfix)