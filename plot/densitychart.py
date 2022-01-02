import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def densitychartTextBlob(inputJsonList, labels, title, outputFile='none', show=False):
    for i in range(0, len(inputJsonList)):
        df = pd.read_json(inputJsonList[i], convert_dates=False)
        print(labels[i] + 'variance: ' + str(df['polarity'].var()))
        print(labels[i] + 'mean: ' + str(df['polarity'].mean()))

        #In statistics, kernel density estimation (KDE) is a non-parametric way to estimate the probability density function of a random variable.
        sns.kdeplot(
            df['polarity'],
            fill=True,
            #common_norm= False,
            #cumulative=True
        )

    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.xlim(-1,1)
    plt.grid()
    plt.xlabel('polarity')
    plt.ylabel('density')
    plt.title(title)
    plt.legend(labels)

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()


def densitychartVader(inputJsonList, labels, title, outputFile='none', show=False):
    for i in range(0, len(inputJsonList)):
        df = pd.read_json(inputJsonList[i], convert_dates=False)
        print(labels[i]+'variance: ' + str(df['compound'].var()))
        print(labels[i]+'mean: ' + str(df['compound'].mean()))


        # In statistics, kernel density estimation (KDE) is a non-parametric way to estimate the probability density function of a random variable.
        sns.kdeplot(
            df['compound'],
            fill=True,
            
            # common_norm= False,
            # cumulative=True
        )

    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.xlim(-1, 1)
    plt.grid()
    plt.xlabel('compound')
    plt.ylabel('density')
    plt.title(title)
    plt.legend(labels)

    if outputFile != 'none':
        plt.savefig(outputFile)
    if show:
        plt.show()
    plt.close()