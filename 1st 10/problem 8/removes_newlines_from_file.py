# Read in the file
with open('data.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('\n', '')

# Write the file out again
with open('data.txt', 'w') as file:
  file.write(filedata)


with open('data.txt','r')as file:
    data = file.read()
    print("data is: " + data)

