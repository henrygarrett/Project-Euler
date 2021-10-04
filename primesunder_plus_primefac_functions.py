import math
def primefac(n):#returns list of prime factors with correct cardinality
    divisor = [n]
    again = True
    while again:
        again = False
        for i in divisor:
            check = math.floor(math.sqrt(i))
            while check > 1:
                if i%check == 0:
                    divisors = check
                    break
                else:
                    check -= 1
            if check == 1:
                divisors = i
            if divisors != i:
                #print(divisor)
                again = True
                divisor.append(int(i/divisors))
                divisor.append(int(divisors))
                divisor.remove(i)
    return divisor
def primesunder(x):#returns lists of primes smaller than or equal to x
    primes = []
    for i in range(x-1):
        if len(primefac(i+2)) == 1:
               primes.append(i+2)
    return primes

