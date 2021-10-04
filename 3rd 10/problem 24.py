#complete
perm = ""
lis = [0,1,2,3,4,5,6,7,8,9]
prod = 10*9*8*7*6*5*4*3*2*1
remainder = 0
for i in range(10,0,-1):
    prod /= i
    for n, item in enumerate(lis):
        if (n+1)*prod + remainder >= 1000000:
            perm = perm + str(item)
            lis.remove(item)
            remainder += n*prod
            break
print(perm)
