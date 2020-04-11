import codecs
import csv

with codecs.open("data.csv", "r", "utf-8") as csvFile:
    fileReader = csv.reader(csvFile, delimiter="," , quotechar="\"")
    for row in fileReader:
        print(row)
