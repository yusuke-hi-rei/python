
def getPrime(max):
    for i in range(2, max + 1):
        flg = True
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                flg = False
                break
        if flg:
            yield i

fn = getPrime(100)
print("first:  " + str(next(fn)))
print("second:  " + str(next(fn)))
print("third:  " + str(next(fn)))


#for n in getPrime(100):
#    print(n, end=" ")

                    
