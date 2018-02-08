"""The script merges files: file1,file2,file3 and creates a file named as the current date"""
import datetime
def merge_files():
    with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w+') as write_file:
        for i in range(3):
            i=i+1
            with open("file"+str(i)+".txt",'r') as read_file:
                write_file.write(read_file.read()+"\n")
merge_files()
