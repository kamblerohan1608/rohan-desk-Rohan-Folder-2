
# write mode  :  (w mode)

# w mode will create a file if it does not exist 
# if file already exists it will overright the file.

# with open("test1.txt","w") as file:
#     data = input("Enter the value : ")
#     file.write(data)

import os

print(os.getcwd())

os.chdir(r"C:\Users\admin\Desktop")

file = open("test.txt","w")
data = "123456789"
file.write(data)
file.close()
