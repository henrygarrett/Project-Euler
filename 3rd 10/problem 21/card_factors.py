import math
from primesunder_plus_primefac_functions import primefac
def card_factors(n):
    factors = []
    for num, i in enumerate(list(dict.fromkeys(primefac(n)))):
        j = 1
        factors.append([1])
        while True:
            if n%i == 0:
                n = n/i
                factors[int(num)].append(i**j)
                j += 1
            else:
                break
    return factors

print(card_factors(1))
print(primefac(1))
