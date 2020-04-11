print("===============ファイル書き込み連続テスト===================")

with open("samplewrite.txt", "w") as f:
    while True:
        msg = input("input test: ")
        if msg == "":
            break;
        f.write(msg + "\n")
    print("Save all messages!")

print("===============UTF-8ファイル書き込み連続テスト===================")
import codecs

with codecs.open("samplewrite.txt", "w", "utf-8") as f:
    while True:
        msg = input("input test: ")
        if msg == "":
            break;
        f.write(msg + "\n")
    print("Save all utf-8 messages!")
