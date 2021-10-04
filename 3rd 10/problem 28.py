sumt = 1
for n in range(2,1002):
    if n%2 == 1:

        sumt = sumt + 4*(n**2) - 6*(n-1)
        #print(str(n) + ':' + str(sumt))
print(sumt)
