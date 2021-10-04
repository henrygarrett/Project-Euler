#complete
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

def nthprime(n):#returns nth prime
    primes = []
    q = 2
    while len(primes) < n:
        if len(primefac(q)) == 1:
            primes.append(q)
            #print(q)
        q += 1
    return primes[n-1]
print(nthprime(10001))
               
