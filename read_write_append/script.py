with open("example.txt", 'a+') as file:
    file.write("hi")
    file.seek(0) #important, it places the pointer at the beginning, because when writing the pointer is moved
    content=file.read()
    print(content)
