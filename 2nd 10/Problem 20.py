#complete
factorial = 1
for n in range(1,101):
    factorial *= n
print(factorial)
sumt = 0
for char in str(factorial):
    sumt += int(char)
print(sumt)
    
