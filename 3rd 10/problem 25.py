#complete
import math
import decimal
def fibnth(n):
    return decimal.Decimal(1/math.sqrt(5))*decimal.Decimal(((1+math.sqrt(5))/2))**(n+1)-decimal.Decimal(1/math.sqrt(5))*decimal.Decimal(((1-math.sqrt(5))/2))**(n+1)
nth = 1
while True:
    if fibnth(nth-1) > 10**999:
        print(nth)
        break
    else:
        nth += 1

               
    
