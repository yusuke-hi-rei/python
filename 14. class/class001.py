#!
#! Class.
#!

class MyObj:
  message = "OK"

  # self is this pointer(near). 
  def print(self):
    print(self.message)

obj = MyObj()
obj.message = "Hello Python!!"
obj.print()
