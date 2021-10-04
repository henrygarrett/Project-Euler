max_length = 1
for i in range(1000000,2,-1):
    length = 1
    if i%5000 == 0:
        print("Start:" + str(i))
    while True:
        if i == 1:
            if length > max_length:
                max_length = length
            break
        length += 1
        if i%2 == 0:
            i = int(i/2)
        else:
            i = 3*i + 1
