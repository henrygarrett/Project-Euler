#complete but very slow
import math
upper = 1000
for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if i**2+j**2==k**2 and i+j+k==1000:
                print("product:" +  str(i*j*k))
