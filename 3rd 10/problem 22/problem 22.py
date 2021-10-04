#complete
with open("data.txt","r") as file:
    file = file.read()
    data = file.split(",")
sumt = 0
data.sort()
for n , entry in enumerate(sorted(data)):
    dumt = 0
    for i in range(1,len(entry)-1):
        dumt += int(ord(entry[i])) - 64
    sumt += dumt*(n+1)

print(sumt)
    
    
