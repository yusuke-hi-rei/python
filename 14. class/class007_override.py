#!
#! Class.
#!

class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return "[Person] My name is " + self.name + "."

class Human(Person):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return "[Human] My name is " + self.name + "."\
           "I am " + str(self.age) + " years old."

ob = Person("Taro")
print(ob)

ob2 = Human("Hanako", 28)
print(ob2)

a = isinstance(ob2, Person)
print(a)

a = isinstance(ob, Human)
print(a)
