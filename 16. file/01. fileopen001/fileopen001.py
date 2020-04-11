print("================ File open test ================")

f = open("sample.txt", "r")
# ファイルを開きファイルオブジェクトを作成する
# テキストを1000文字読み込む
result = f.read(1000)
print(result)
# ファイルを閉じる(必ず忘れないように)
f.close()

print("================ 全て読み込む ================")

f = open("sample.txt", "r")
# Read()の引数なしはファイルサイズ分読み込む。
result = f.read()
print(result)
f.close()

print("================ with を使ったファイル読込 ================")
with open("sample.txt", "r") as f:
    result = f.read()
    print(result)
# with を使用すると構文を抜ける段階でclose()される。

print("================ １行ずつ読込 ================")
with open("sample.txt", "r") as f:
    n = 1
    for line in f:
        # strip: white space, new line deleted.
        print(str(n) + " : " + line.strip())
        n += 1
    
