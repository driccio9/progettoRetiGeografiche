emoticonsPositive = ('😇','😊','❤️','😘','💞','💖','🤗','💕','👏','🎉','👍','🔝')
emoticonsNegative = ('😂','😡','😠','😭','🤦‍','🤷🏼‍','😞','😱','😓','👎')

radiciPositive = ("ama","amo","affett","allegr","amabil","apprezz","armon","affet",
                  "applaus","abbracc","ador",
                  "bell","ben","beat","brav","buon","benef","brill",
                  "cuor","coeren","celebr",
                  "dolc","divert",
                  "evviva","emoz","elog",
                  "felic","fest","facil",
                  "gentil","god","grazi","generos","gioi",
                  "innamor", "interes","insieme",
                  "libert",
                  "maestos","miglior",
                  "pace","passion","perfe","piac","pura","purezz","prezios","promuov",
                  "rilass","riabbracc",
                  "solida","spero","speran","success","sì","sacr","stupend","spettacol",
                  "viv","vin","valor","vale","vera","vittor")
radiciNegative = ("accus","amaro","amarez","arm","ammazz",
                  "brut","boicott","boh","bho",
                  "condann","cazz","crisi","critic","coglion",
                  "decent","depress","detest","disgr","delir","damn","drog",
                  "fumo","fuma",
                  "esorcis",
                  "fascis",
                  "guai",
                  "immat","insult", "inuman","impone",
                  "lent",
                  "mor","merd","male","maial",
                  "no", "nega","ncazz","negr",
                  "od","oscur",
                  "perde","preoccup","pusillanim","porc",
                  "rovina",
                  "schif","satan","sprof","soffri","soffer","scandal","scars","sporc", "spar","stalk",
                  "trist","trash","tarocc",
                  "vergogn",
                  "zitt")
radiciDaEscludere = ("now", "nom", "not","noz", "amp", "nor","veramente","imponent")

import csv

listtxt = []
i = 1

with open('vader_lexicon.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        i = i + 1
        translate = row[0]
        listtxt.append({'text': translate, 't2': row[1], 't3': row[2], 'text4': row[3]})
        print(translate + "\t" + row[1] + "\t" + row[2] + "\t" + row[3])

print(len(listtxt))

positive = "0.9"
positive2 = "1.92094"
positive3 = "[1, 4, -3, 1, 2, 1, 2, -2, 2, 1]"

negative = "-2.3"
negative2 = "1.1"
negative3 = "[-4, -3, -4, -1, -2, -2, -1, -2, -1, -3]"

with open('vader_lexicon2.txt', mode='w') as filevader:
    writer = csv.writer(filevader, delimiter='\t')

    for row in listtxt:
        if row["text"] != "":
            writer.writerow([row["text"], row["t2"], row["t3"], row["text4"]])

    for a in emoticonsPositive:
        writer.writerow([a, positive, positive2, positive3])

    for a in radiciPositive:
        writer.writerow([a, positive, positive2, positive3])

    for a in emoticonsNegative:
        writer.writerow([a, negative, negative2, negative3])

    for a in radiciNegative:
        writer.writerow([a, negative, negative2, negative3])
