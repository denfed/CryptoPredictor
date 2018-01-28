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
# This script reads a GPS track in CSV format and
#  prints a list of coordinate pairs
import csv

# Set up input and output variables for the script
file = open("crypto-markets.csv", "r")

# Set up CSV reader and process the header
csvReader = csv.reader(file)

# Make an empty list
coordList = []

# Loop through the lines in the file and get each coordinate
for row in csvReader:
    name = row[0]
    if name not in coordList:
        print(name)
        coordList.append([name])

# Print the coordinate list
print(coordList)