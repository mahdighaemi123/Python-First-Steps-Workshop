count = int(input("count: "))
print(count)

my_list = []
print(my_list)

for _ in range(count):
    num = int(input("num: "))

    my_list.append(num)

    print(num)
    print(my_list)


my_sum = sum(my_list)
my_len = len(my_list)
my_avg = my_sum / my_len

print(my_sum)
print(my_len)
print(my_avg)