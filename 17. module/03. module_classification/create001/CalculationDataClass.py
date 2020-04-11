class CCalcData:
    def __init__(self, fname="sample.txt"):
        self.data = []
        self.filename = fname
        self.func = lambda x: x

    def __str__(self):
        return "<CCalcData filename=" + self.filename + \
               "data=" + str(self.data) + ">"

    # 読込
    def read(self, fname=None):
        if fname != None:
            self.filename = fname

        try:
            with open(self.filename, "r") as reader:
                for line in reader:
                    try:
                        self.data += [int(line.strip())]
                    except ValueError:
                        self.data += [0]
        except Exception as error:
            print(error)
        print(self.data)

    # 書き込み
    def write(self, fname=None):
        if fname != None:
            fpath = fname
        else:
            fpath = self.filename
            
        try:
            with open(fpath, "w") as writer:
                for item in self.data:
                    writer.write(str(item) + "\n")
        except Exception as error:
            print(error)

    # 更新
    def update(self, fn=None, save=False):
        if fn != None:
            self.func = fn
        data2 = []
        for item in self.data:
            data2 += [self.func(item)]
        if save:
            self.data = data2
        return data2

    # 計算
    def calc(self):
        total = 0
        for item in self.data:
            total += item
        return {"total":total, "ave":total//len(self.data) }
