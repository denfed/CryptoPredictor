import json
import codecs
import getCurrencyNames as g
import datetime
import matplotlib.pyplot as p
import numpy as np
import tkinter as tk

data = []
unixtime = []
currList = g.getNames()
currList.pop(0)
master = []

with codecs.open('output.json', 'rU', 'utf-8') as f:
    for line in f:
        data.append(json.loads(line))

for a in data:
    time = datetime.datetime.fromtimestamp(a['time']).strftime('%Y-%m-%d')
    master.append([time,' ' + a['matched'] + ' ', a['sentiment']])
print(master)

#time = datetime.datetime.fromtimestamp(1284101485).strftime('%Y-%m-%d')
match = []
priceC = 0
import csv
file = open("crypto-markets-trimmed.csv", "r")
csvReader = csv.reader(file)
date = []
for row in csvReader:
    try:
        priceC = float(row[8])-float(row[5])
        date.append([' ' + row[0] + ' ', row[3], priceC])
    except:
        pass
for i in range (1, len(master) - 1):
    for num in range (1, len(date) - 1):
        if date[num][1] == master[i][0] and date[num][0] == master[i][1]:
            match.append([master[i][2], date[num][2]])
xPlt = []
yPlt = []

# sentiment
for temp in range (1, len(match)-1):
    xPlt.append(match[temp][0])

# price change
for temp in range (1, len(match)-1):
    yPlt.append(match[temp][1])

p.figure('regression')
fit = np.polyfit(xPlt, yPlt, 1)
fit_fn = np.poly1d(fit)
ya = fit_fn(xPlt)
p.plot(xPlt, yPlt, 'yo', xPlt, ya, '--k')
p.title('Stock Value vs. Sentiment Polarity')
p.show(block = False)
p.show(block = True)


