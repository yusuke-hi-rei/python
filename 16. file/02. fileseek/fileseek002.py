print("===========ファイル位置を移動してファイルを読み込む===========")

import codecs
import os

try:
    with codecs.open("sampleseek.txt", "r", "utf-8") as f:
        while True:
            n = input("input number: ")
            if n == "":
                break
            try:
                num = int(n)
            except ValueError:
                num = 0
            f.seek(10 * num, os.SEEK_SET)
            try:
                result = int(f.read(9))
            except ValueError as error:
                print(error)
                result = 0
            print("data: " + str(result))
except Exception as error2:
    print("[ERROR]" + str(error2))
    
