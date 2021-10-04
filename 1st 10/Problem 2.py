Sum = 0
x1 = 1
x2 = 2
while max(x1,x2) <= 4000000:
    if x1%2==0:
        Sum += x1
    if x2%2==0:
        Sum += x2
    x1 = x1 + x2
    x2 = x1 + x2
print(Sum)
#complete
