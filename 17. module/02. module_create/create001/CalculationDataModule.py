data = []
# ファイル名
filename = "sample.txt"
func = lambda x: X

# 読込
def read(fname=filename):
    # global変数で関数外の変数へアクセスする
    global data
    global filename
    filename = fname

    try:
        with open(filename, "r") as reader:
            for line in reader:
                try:
                    data += [int(line.strip())]
                except ValueError:
                    data += [0]
    except Exception as error:
        print(error)

# 書き込み
def write(fname=filename):
    global data
    try:
        with open(fname, "w") as writer:
            for item in data:
                writer.write(str(item) + "\n")
    except Exception as error:
        print(error)

# 更新
def update(fn=func, save=False):
    global data
    global func
    func = fn
    data2 = []
    for item in data:
        data2 += [func(item)]
    if save:
        data = data2
    return data2

# 計算
def calc():
    global data
    total = 0
    for item in data:
        total += item
    return {"total":total, "ave":total//len(data) }


