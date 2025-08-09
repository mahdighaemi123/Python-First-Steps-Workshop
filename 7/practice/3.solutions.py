# solution 1
from collections import Counter
colors = input()
my_list = colors.split(" ")

my_dict = {}

for color in my_list:
    if color not in my_dict:
        my_dict[color] = 1
    else:
        my_dict[color] += 1

print(my_dict)

# solution 2
my_list = input().split()
my_dict = {}

for color in my_list:
    my_dict[color] = my_dict.get(color, 0) + 1

print(my_dict)

# solution 3

my_list = input().split()
my_counter = Counter(my_list)

print(my_counter)
