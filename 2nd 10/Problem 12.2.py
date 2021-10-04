#complete
import math
from primesunder_plus_primefac_functions import primefac
nth = 5
while True:
    sumt = int(0.5*nth*(nth+1))
    #sumt = 2303731
    divisor = 1
    for i in list(dict.fromkeys(primefac(sumt))):
        n = sumt
        j = 1
        while True:
            if n%i == 0:
                n = n/i
                j += 1
            else:
                break
            
        divisor *= j
    if divisor > 500:
        print(sumt)
        break
    nth += 1

