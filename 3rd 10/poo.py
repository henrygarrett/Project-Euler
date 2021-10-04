import math
def isabundant(n):
    if sum(i for i in range(1,math.floor(n/2)+1) if n%i == 0) > n:
        return True
    else:
        return False
n = 1
while True:
    if n%1000 == 0:
        print(n)
    if isabundant(n) and n%6 == 3 :
        print(str(n) + ": " +  str(3))
    n += 1
