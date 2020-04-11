#!
#! Exceptions. raise
#!

class MyError(Exception):
    def __init__(self, msg, val):
        self.args = (msg, val)

    def __str__(self):
        return str(self.args[0]) + " : " + str(self.args[1])

def fn(num):
    try:
        n = int(num)
    except Exception:
        if num == "":
            print("........")
            n = 0
        else:
            raise MyError("error: ", num)
    return n

num = input("input value: ")
try:
    num2 = fn(num)
    result = num2 * num2
    print(str(num) + " : " + str(result))
except MyError as err:
    print(err)
