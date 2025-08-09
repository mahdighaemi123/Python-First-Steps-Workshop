a = 10
b = 20

# solution 1
a, b = b, a

# solution 2
a = 10
b = 20

a = a + b
b = a - b
a = a - b

# solution 3
a_copy = a
b_copy = b

a = b_copy
b = a_copy
