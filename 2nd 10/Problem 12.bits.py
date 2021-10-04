import math
from primesunder_plus_primefac_functions import divisors
sumt = 60
divisor = [sumt]
n = len(divisor)
for i in divisor:
    check = max(math.floor(0.5*i),1)
    while check > 1:
        #print(check)
        if i%check == 0:
            divisors = check
            check -= 1
            break
        check -= 1
    if check == 1:  
        divisors = i
        #print(divisor)
    again = True
    divisor.append(int(i/divisors))
    divisor.append(int(divisors))
    divisor = list(dict.fromkeys(divisor))
print(divisor)  
