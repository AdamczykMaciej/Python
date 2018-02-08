file = open("./fruits.txt", 'r')
content = file.read()
print(content)

file.seek(0)
content = file.readlines()
file.close() #closes the file which we are reading
print(content)

content = [i.rstrip("\n") for i in content]
print(content)
for i in content:
    print (len(i))
