import text2emotion as te
import pandas as pd


def text2emotion(dataFrame:pd.DataFrame, outPathFile:str):
    emotions = dataFrame['text'].map(te.get_emotion).tolist()
    dataFrame = pd.concat([dataFrame, pd.DataFrame(emotions)], axis=1)
    dataFrame.to_json(outPathFile, orient='records')


#Prova#########
df = pd.read_json(r'alltweet.json', date_unit='s')
text2emotion(df, r'sample/text2emotionAllTweet.json')
################

inputsFiles = [
    ''
]
