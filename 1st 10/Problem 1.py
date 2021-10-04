Num = 0
for i in range(1000):
        if i%3==0:
            Num += i
        if i%5==0:
            Num += i
        if i%15==0:
            Num -= i
print(Num)
#works
