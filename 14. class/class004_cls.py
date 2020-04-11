#!
#! Class.
#!

class MyObj:
  message = "OK"

  @classmethod
  def print(cls):
    print(cls.message)

MyObj.print()
MyObj.message = "Welcome!"
MyObj.print()
