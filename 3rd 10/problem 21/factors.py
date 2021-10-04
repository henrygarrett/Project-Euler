import math
from card_factors import card_factors
from itertools import product
print(card_factors(420))
def factors(n):
    print("boo")
    iterator = []
    print(card_factors(1))
    print(card_factors(n))
    prime_list = card_factors(n)
    factor = []
    for i in range(len(prime_list(n))):
        print(i)
        iterator.append("var" + str(i))
    for iterator in product(*card_factors(n)):
        print(iterator)
        factor.append(math.prod(iterator))
    return factor

print(factors(1))
