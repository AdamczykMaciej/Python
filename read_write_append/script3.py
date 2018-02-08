
import datetime
"""
This script creates an empty file.
"""
filename=datetime.datetime.now()
#Creates an empty file
def create_file():
    """This function creates an empty file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f"),"w") as file:
        file.write("") #Writing an empty string
create_file()
for i in range(5):
    print("Makaroni")
