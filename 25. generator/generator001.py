
def getPrime(max):
    for i in range(2, max + 1):
        flg = True
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                flg = False
                break
        if flg:
            yield i

for n in getPrime(100):
    print(n, end=" ")

                    
