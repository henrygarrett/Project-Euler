import math
from primesunder_plus_primefac_functions import primefac
from card_factors import card_factors
def fac(n):#returns list of factors
    if n == 1:
        return [1]
    else:
        divisor = [n]
        again = True
        previous = 0
        while again:
            again = False
            for i in divisor:
                check = max(math.floor(math.sqrt(i)),1)
                while check > 0:
                    #print(check)
                    if i%check == 0:
                        divisors = check
                        break
                    check -= 1
                if divisors != i:
                    #print(divisors)
                    #print(int(i/divisors))
                    again = True
                    x = int(n/divisors)
                    divisor.append(int(x))
                    divisor.append(int(divisors))
                    divisor.append(int(i/divisors))
                    divisor = list(set(divisor))
                print(divisor)
            if len(list(set(divisor))) == card_factors(n):
                return list(set(divisor))
            previous = len(divisor)
print(fac(220))
