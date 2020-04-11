#!
#! Make function.
#!

def hello(name = "noname", age = 0):
  print("Hi, I am " + name + " (" + str(age) + ").")

hello("TestName", 30)
hello(name = "Google", age=28)
hello()
