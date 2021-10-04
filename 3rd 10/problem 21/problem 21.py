import math
from factors import factors
fac_list = []
sumt = 0
for n in range(1,10001):
    print(n)
    fac_list.append(sum(x for x in factors(n) if x != n))
    if n%10 == 0:
        print(n)
for i in range(2,len(fac_list)+1):
    if i < 50 or i > 9950:
        print(i)
    if fac_list[i-2] == sum(x for x in factors(fac_list[i-2]) if x != fac_list[i-2] + 1):
        sumt += i
print(sumt)
    
    
       
