check = []
m = 1000000
for i in range(1,m+1):
    check.append(i)
max_length = 1
mac_length = 1
print(check[999999])
for i in check:

    length = 1
    mac = i
    n = i
    while True:
        if n == 1:
            if length >= max_length:
                max_length = length
                mac_length = mac
            break
        length += 1
        if n%2 == 0:
            if n <= m:
                check[n-1] = 1
                n = check[int(n/2)-1]
            elif n/2 <= m:
                n = check[int(n/2)-1]              
            else:
                n = int(n/2)
        else:
            if 3*n + 1 <= m:
                check[n-1] = 1
                n = check[3*n]
            elif n <= m:
                check[n-1] = 1
                n = 3*n+1                
            else:
                n = 3*n+1

print(mac_length)
