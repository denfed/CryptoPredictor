'''def getNames():
    concl = []
    for I in open('crypto-markets.csv', 'r').readlines():
        str(I)
        string = I[0]
        print(string)
        if string not in concl: concl += string
    print(concl)
    return concl

if __name__ == '__main__':
    getNames()
'''

import csv

def getNames():
    file = open("crypto-markets-trimmed.csv", "r")
    csvReader = csv.reader(file)
    nameList = []
    for row in csvReader:
        name = ' ' + row[0] + ' '
        if name not in nameList:
            nameList.append(name)
    return nameList

if __name__ == '__main__':
    getNames()