import csv

listtxt = []
i = 1

with open('../vader_lexicon2.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        i = i + 1
        # if i > 203:
        #    translate = cleanedFunction.translate(row[0])
        # else:
        translate = row[0]
        listtxt.append({'text': translate, 't2': row[1], 't3': row[2], 'text4': row[3]})
        print(translate + "\t" + row[1] + "\t" + row[2] + "\t" + row[3])

print(len(listtxt))

with open('../vader_lexicon2.txt', mode='w') as filevader:
    writer = csv.writer(filevader, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in listtxt:
        if row["text"] != "":
            writer.writerow([row["text"], row["t2"], row["t3"], row["text4"]])
