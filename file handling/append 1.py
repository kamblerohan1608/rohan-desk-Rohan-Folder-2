
# append mode :  a mode

# a mode will create a file if not existing.
# if already exists it will add the data at the end of that file.

with open("test1.txt","a") as file:
    data = "\nThis is addition to existing data 2"
    file.write(data)

