print("===============例外処理を含むファイルオープン==================")
import codecs

try:
    # "w" を "r"にして失敗させる
    with codecs.open("exceptionsample.txt", "r", "utf-8") as f:
    # with codecs.open("exceptionsample.txt", "w", "utf-8") as f:
        msg = input("input test: ")
        f.write(msg + "\n")
        print("Save message!")
except Exception as error:
    print("[ERROR]" + str(error))
