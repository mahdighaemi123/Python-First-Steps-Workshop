# helper functions for list

# map
# apply a function on all elements in list

def make_it_int(x):
    return int(x)

l = ["1", "2", "3"]
l = map(make_it_int, l)

l = ["1", "2", "3"]
l = map(int, l)

# filter
# get element wich return true when applying a function
def is_even(x):
    return int(x) % 2 == 0

l = ["1", "2", "3"]
l = filter(is_even, l)

l = ["1", "2", "3"]
l = filter(lambda x: int(x) % 2 == 0, l)
