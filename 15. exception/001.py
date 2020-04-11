#!
#! Exceptions.
#!

data = [
  ("Taro", "yamada@taro"),
  ("Hanako", "hana@flower"),
  ("Sachiko", "sachi@happy"),
  ("Ichiro", "ichi@roo")
  ]

n = input("input value: ")

msg = ""
try:
  n = int(n)
  result = data[n]
except ValueError as error1:
  result = ("[E1]:",) + error1.args
except IndexError as error2:
  result = ("[E2]:",) + error2.args
except Exception as error3:
  result = ("[E3]:",) + error3.args

print(result)
