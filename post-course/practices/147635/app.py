# https://quera.org/problemset/147635/

count = int(input())
numbers = input().split()

for number in numbers:
    number = int(number)

    if number > 15:
        print("cooler")
    else:
        print("heater")