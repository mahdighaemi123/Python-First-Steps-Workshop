# Files:
# saving data in computers hard

import os  # for working with files needed

# List files and directories in a given path
print(os.listdir(r".\4\practice"))         # Relative path
print(os.listdir(r"E:\Desktop\PyClass2"))  # Absolute path

# Opening and Reading Files:
f = open("my_data.txt")      # Open file for reading (default mode)
content = f.read()           # Read the entire file content into a string
f.close()                    # Always close the file!

# Recommended: Use 'with' statement to auto-close the file
with open("my_data.txt") as f:
    print(f.read())

# Reading a UTF-8 encoded file, for persion text is needed
with open("my_data.txt", encoding="utf-8") as file:
    print(file.read())


# Modes in opening a file:
# 'r' = read (default)
# 'w' = write (overwrites)
# 'a' = append (to the end)

with open("my_data.txt", "r", encoding="utf-8") as file:
    print(file.read())  # Print text content of file

with open("my_data.txt", "w", encoding="utf-8") as file:
    file.write("123")  # Overwrites file with "123"

with open("my_data.txt", "a", encoding="utf-8") as file:
    file.write("123")  # Adds "123" to the end
