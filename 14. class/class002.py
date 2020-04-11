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

obj = MyObj("Hello!")
obj.print()
