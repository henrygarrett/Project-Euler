import math
def isabundant(n):
    if sum(i for i in range(1,math.floor(n/2)+1) if n%i == 0) > n:
        return True
    else:
        return False
abundants = []
for num in range(28123+2):
    if isabundant(num):
        if num%6 == 2:
            abundants.append(num)
        elif num%6 == 3:
            abundants.append(num)
        elif num%6 == 4:
            abundants.append(num)
print("Length of abundants: " + str(len(abundants)))
sumt = []
for i in abundants:
    for j in abundants:
        if i + j < 28124 and ( (i + j)%6 == (1 or 5)):
            sumt.append(i+j)
print("Length of sumt: " + str(len(sumt)))
sumt = list(dict.fromkeys(sumt))
print("Length of sumt: " + str(len(sumt)))
notsumt = []
# finding nots sums mod = 1 and 5 over 956
for i in range(28123+2):
    if (i%6 == (1 or 5)) and i > 956:
        notsumt.append(i)
for i in sumt:
    notsumt.remove(i)
# adding certain mods below minimum
for x in range(956):
    if x%6 == (1 or 3 or 5):
        notsumt.append(x)
for x in range(51):
    if x%6 == 4:
        notsumt.append(x)
for x in range(31):
    if x%6 == 2:
        notsumt.append(x)
for x in range(23):
    if x%6 == 0:
        notsumt.append(x)
print("sum of notsumt: " + str(sum(notsumt)))
