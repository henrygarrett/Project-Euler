#complete
import math
n = 21
triangle = []
for level in range(n):
    #print("Level: " + str(level))
    triangle.append([])
    for n in range(level+1):
        if n == 0:
            #print(str(n) + " 1")
            triangle[level].append(1)
        elif n == level:
            #print(str(n) + " 1")
            triangle[level].append(1)
        else:
            #print(str(n) + " " + str(triangle[level-1][n-1]+triangle[level-1][n]))
            triangle[level].append(triangle[level-1][n-1]+triangle[level-1][n])
    print(triangle[level])
sumt = 2            
for i in range(1,20):
    sumt += triangle[20][i]**2
        
print(sumt)
