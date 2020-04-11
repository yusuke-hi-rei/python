#!
#! Class.
#!

class MyObj:
  # __init__ is constructor(near). 
  def __init__(self, msg):
    self.message = msg

  # Object string display.
  def __str__(self):
    return "<MyObj: message= " + self.message + " >"

  # Property
  @property
  def message(self):
    return self.__message

  # Functions for changing property values
  @message.setter
  def message(self, value):
    if value != "":
      self.__message = value
    

ob = MyObj("Hello")
print(ob.message)
ob.message = ""
print(ob)
ob.message = "Bye!"
print(ob)
