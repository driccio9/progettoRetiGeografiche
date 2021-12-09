import text2emotion as te
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json(r'sample.json')
df['emotions'] = df.cleanedEnglishText.map(te.get_emotion)

meanEmotions = {
    'Happy': .0,
    'Angry': .0,
    'Surprise': .0,
    'Sad': .0,
    'Fear': .0
}

for row in df['emotions']:
    for k, v in row.items():
        meanEmotions[k] += (v / df.shape[0]) * 100

#pie cahart
labels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
values = [meanEmotions['Happy'], meanEmotions['Angry'], meanEmotions['Surprise'], meanEmotions['Sad'], meanEmotions['Fear']]
patches, texts, junk = plt.pie(values, labels=labels,  startangle=90, autopct='%.2f')
plt.style.use('default')
plt.title("Text to Emotion Result")
plt.axis('equal')
plt.show()