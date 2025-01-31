# writelines()
with open("users_2.txt", "w") as f:
    lines = ["Python is great\n", "File handling in Python\n", "writelines() method is useful\n"]
    f.writelines(lines)  

with open("users_2.txt", "r") as f:
    print(f.read())  

# tell()
with open("users_2.txt", "r") as f:
    print("Initial position:", f.tell()) 
    content = f.read(10)  
    print("After reading 10 chars, position:", f.tell()) 

# seek()
with open("users_2.txt", "r") as f:
    f.seek(0, 2)  # Move to the end of the file
    print("Final position:", f.tell())




