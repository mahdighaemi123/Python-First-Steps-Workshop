# list comprehension
# create a list in one line

list = []

for x in range(1, 10):
    list.append(x**2)


list = [x**2 for x in range(1, 10)]
