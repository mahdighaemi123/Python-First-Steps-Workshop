# https://quera.org/problemset/87176/

def game(number):
    number_str = str(number)

    nums = list()

    for num_str in number_str:
        num = int(num_str)
        nums.append(num)

    bigest = max(nums)
    lowest = min(nums)

    result = bigest - lowest

    print(result)
    return result

# tests
# game(17)# -> 6
# game(99)# -> 0
# game(91)# -> 8
