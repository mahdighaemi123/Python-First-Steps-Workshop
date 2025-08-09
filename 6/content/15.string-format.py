# string format:
# create text string from my data

name = "mahdi"

# Concatenate strings (classic way)
message = "my name is " + name

# Using f-string (modern & recommended)
message = f"my name is {name}"

# Using %-formatting (old school, still works)
message = "my name is %s" % name

# Using str.format() (Python 2.7+ and 3+)
message = "my name is {}".format(name)
