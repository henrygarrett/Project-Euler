#works
import math
sumt = 0
n = 2000000
for i in range(2,n-1):
    check = math.floor(math.sqrt(i))
    while check > 1:
        if i%check == 0:
            break
        else:
            check -= 1
    if check == 1:
        sumt += i
print(sumt)
