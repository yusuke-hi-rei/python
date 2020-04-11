import codecs
import csv

with codecs.open("data.csv", "a", "utf-8") as csvFile:
    fileWriter = csv.writer(csvFile, delimiter="," , quotechar="\"")
    while True:
        instr = input("input data")
        if instr == "":
            break
        data = instr.split(",")
        fileWriter.writerow(data)

    print("data writing is over..")
