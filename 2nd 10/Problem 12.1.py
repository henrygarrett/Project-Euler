import math
nth = 1
while True:
    sumt = int(0.5*nth*(nth+1))
    divisor = [60]
    again = True
    check = max(math.floor(0.5*sumt),1)
    while again:
        n = len(divisor)
        again = False
        for i in divisor:
            check = max(math.floor(0.5*i),1)
            while check > 1:
                #print(check)
                if i%check == 0:
                    divisors = check
                    check -= 1
                    break
                check -= 1
            if check == 1:  
                divisors = i
            if divisors != i:
                #print(divisor)
                again = True
                divisor.append(int(i/divisors))
                divisor.append(int(divisors))
                divisor = list(dict.fromkeys(divisor))

            if len(divisor) == n:
                again = False
        
        
    if len(divisor) == 499:
        print(sumt)
        break
    print(len(divisor))
    print(divisor)
    nth += 1
