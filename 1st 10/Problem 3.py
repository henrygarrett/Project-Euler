import math
n = 600851475143
divisor = [n]
again = True
def divisors(x):
    check = math.floor(math.sqrt(x))
    while check >= 3:
        if x%check == 0:
            return check
            break
        else:
            check -= 1
    return x


while again:
    again = False
    for i in divisor:
        if divisors(i) != i:
            again = True
            divisor.append(int(i/divisors(i)))
            divisor.append(int(divisors(i)))
            divisor.remove(i)       
    divisor = list(dict.fromkeys(divisor))


print("divisors of " + str(n) + ": " + str(divisor))
print("max divisor: " + str(max(divisor)))
    
#works
