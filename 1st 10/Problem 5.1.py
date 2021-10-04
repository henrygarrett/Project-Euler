import math
from primesunder_plus_primefac_functions import primefac
from primesunder_plus_primefac_functions import primesunder
lcm = 1
for i in primesunder(20):
    lcm *= i**(math.floor(math.log(20,i)))
print(lcm)
