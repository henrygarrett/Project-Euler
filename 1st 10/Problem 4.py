pali = 0
def ispali(x):
    yes = True
    for i in range(len(str(x))):
        if str(x)[i] != str(x)[-i-1]:
            yes = False
    return yes            
        
for i in range(1000):
    for j in range(1000):
        if i*j >= pali and ispali(i*j):
            pali = i*j

print(pali)
#complete
