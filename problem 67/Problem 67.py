#complete
data = []
with open("data.txt","r") as file:
    for n, line in enumerate(file):
        data.append([])
        for i, num in enumerate(line):
            if i%3 == 0:
                data[n].append(int(line[i] + line[i+1]))
distance = []
for n, level in enumerate(data):
    distance.append([])
    for i, entry in enumerate(data[n]):
        #print(str(n) + str(i))
        #print(distance)
        if n > 0 and 0 < i and i < n:
            distance[n].append(entry + max(distance[n-1][i], distance[n-1][i-1]))
        elif n > 0 and i == 0:
            distance[n].append(entry + distance[n-1][i])
        elif n > 0 and i == n:
            distance[n].append(entry + distance[n-1][i-1])
        elif n == 0:
            distance[n].append(data[n][i])

print("Max weighted path is: " + str(max(distance[99])))
