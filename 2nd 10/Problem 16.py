#complete
string = str(2**1000)
sumt = 0
for i in range(len(string)):
    sumt += int(string[i])
    print(sumt)
