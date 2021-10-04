import math
def primefac(n):#returns list of prime factors with correct cardinality
    divisor = [n]
    again = True
    def divisors(x):
        check = math.floor(math.sqrt(x))
        while check > 1:
            if x%check == 0:
                return check
            else:
                check -= 1
        return x


    while again:
        again = False
        for i in divisor:
            if divisors(i) != i:
                #print(divisor)
                again = True
                divisor.append(int(i/divisors(i)))
                divisor.append(int(divisors(i)))
                divisor.remove(i)       
    return divisor

def primesunder(x):#returns lists of primes smaller than or equal to x
    primes = []
    for i in range(x-1):
        if len(primefac(i+2)) == 1:
               primes.append(i+2)
    return primes
print(primefac(1))
