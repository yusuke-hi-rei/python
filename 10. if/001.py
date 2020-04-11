#!
#! If.
#!

n = 123
if n % 3 == 0:
    result = "even."
else:
    result = "odd."
print(result)   

if 15 <= n and n <= 200:
    result = "OK."
else:
    result = "NG."
print(result)   

if 1000 <= n:
    result = "15<="
elif 200 <= n:
    result = "200<="
elif 100 <= n:
    result = "100<="
else:
    result = "Nothing"
    
print(result) 
