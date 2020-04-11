from datetime import *

print("--------DATETIME---------")
print("--------today---------")
dt = datetime.today()
print(dt)

print("--------current time---------")
dt = datetime.now()
print(dt)

print("--------create date---------")
dt = datetime(2020, 2, 24, 12, 5, 35)
print(dt)

print("--------get date---------")
dt = datetime.now()
result = str(dt.year) + "年" + str(dt.month) + "月" + str(dt.day) + "日"
print(result)

print("--------get time---------")
dt = datetime.now()
result = str(dt.hour) + "時" + str(dt.minute) + "分" + str(dt.second) + "秒"
print(result)

print("\n--------DATE---------")
print("--------today---------")
dt = date.today()
print(dt)

print("--------create date---------")
dt = date(2020, 2, 24)
print(dt)

print("\n--------TIME---------")
print("--------create time---------")
tm = time(10, 15, 35, 30)
print(tm)

print("\n--------TIME Elapsed---------")
dt1 = date.today()
dt2 = date(2010, 2, 27)
result = dt1 - dt2
print(result)

print("\n--------TIME DELTA---------")
dt1 = date.today()
dt2 = dt1 + timedelta(days=1000)
print(dt2)

dt3 = timedelta(days=1, seconds=20, microseconds=333,\
  minutes=1, hours=5, weeks=2)
print(dt3)




