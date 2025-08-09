# https://quera.org/problemset/3539/

number = input()

while len(number) != 1:
    new_number = 0

    for n in number:
        new_number += int(n)

    number = str(new_number)

print(number)