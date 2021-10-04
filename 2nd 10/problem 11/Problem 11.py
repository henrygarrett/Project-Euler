data = []
with open("table.txt","r") as file:
    for n, line in enumerate(file):
        data.append([])
        for i, num in enumerate(line):
            if i%3 == 0:
                add = int(line[i] + line[i+1])
                data[n].append(add)
maxt = 0
print(data)
for i, row in enumerate(data):
    for j, column in enumerate(data[i]):
        if i < 17 and (data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j] > maxt):
            maxt = data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j]
        if i < 17 and j < 17 and (data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3] > maxt):
            maxt = data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3]
        if i < 17 and j > 2 and (data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3] > maxt):
            maxt = data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3]
        if j > 2 and (data[i][j]*data[i][j-1]*data[i][j-2]*data[i][j-3] > maxt):
            maxt = data[i][j]*data[i][j-1]*data[i][j-2]*data[i][j-3]
print(maxt)
