#!
#! Class.
#!

class MyObj:
  # __init__ is constructor(near). 
  def __init__(self):
    # "__"num is private member 
    self.__num = 123
    self.message = "OK!"

  # self is this pointer(near). 
  def print(self):
    print(str(self.__num) + " : " + self.message)

obj = MyObj()
obj2 = MyObj()
obj.__num = 321
obj.message = "Hi!"
obj.print()
obj2.print()
