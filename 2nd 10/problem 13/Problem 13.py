data = []
with open("data.txt","r") as file:
    for n, line in enumerate(file):
        word = ""
        for i, num in enumerate(line):
            if i <= 49:
                word = word + num
        data.append(int(word))
sumt = 0
for num in data:
    sumt += num
    print(sumt)
