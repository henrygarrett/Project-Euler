#complete
check = []
m = 1000000
for i in range(1,m+1):
    check.append(i)
max_length = 1
mac_length = 1
for i in check:
    length = 1
    mac = i
    while True:
        i = int(i)
        #print(i)
        if i == 1:
            if length >= max_length:
                max_length = length
                mac_length = mac
            break
        length += 1
        if i%2 == 0:
            if i <= m:
                #print("part 1")
                if i < mac:
                    check[i-1] = 1
                i = check[int(i/2)-1]
            elif i/2 <= m:
                #print("part 2")
                i = check[int(i/2)-1]              
            else:
                #print("part 3")
                i = int(i/2)
        else:
            if 3*i + 1 <= m:
                #print("part 4")
                if i < mac:
                    check[i-1] = 1
                i = check[3*i]
            elif i <= m:
                #print("part 5")
                if i < mac:
                    check[i-1] = 1
                i = 3*i+1                
            else:
                #print("part 6")
                i = 3*i+1
print(mac_length)
print(max_length)
