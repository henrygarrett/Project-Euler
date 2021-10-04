#complete
import math
def d(n):
    return sum(i for i in range(1,math.floor(n/2)+1) if n%i == 0)
sumt = 0
for i in range(10001):
    if i == d(d(i)) and i != d(i):
        sumt += i    
print(sumt)
