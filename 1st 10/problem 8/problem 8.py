with open('data.txt', 'r') as file :
  filedata = file.read()

maximum = 0
for i in range(len(filedata)-13):
    product = 1
    for j in range(13):
        product *= int(filedata[i+j])
    if product > maximum:
        maximum = product
        
print (maximum)
