import codecs

with codecs.open("encodingfile.txt", "r", "utf-8") as f:
    n = 1
    for line in f:
        print(str(n) + " : " + line.strip())
        n += 1

