#!
#! Class.
#!

class MyObj:
  # __init__ is constructor(near). 
  def __init__(self, msg):
    self.message = msg

  # self is this pointer(near). 
  def print(self):
    print(self.message)
  # + operator.
  def __add__(self, other):
    return MyObj(self.message + " " + other.message)

  # += operator.
  def __iadd__(self, other):
    self.message = self.message + " " + other.message
    return self

  # Object string display.
  def __str__(self):
    return "<MyObj: message= " + self.message + " >"

ob = MyObj("first")
ob2 = MyObj("second")
ob3 = ob + ob2
ob3.print()
ob3 += MyObj("Third")
ob3.print()

print(ob3)
