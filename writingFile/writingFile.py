file=open("example.txt", 'w')
file.write("Line 1\n")
file.write("Line 2\n")


numbers = [1,2,3]
for i in numbers:
    file.write(str(i)+"\n")
i=0
while(i<1000):
    i=i+1
    file.write("Line " + str(i) + "\n")
