# https://quera.org/problemset/129726/

def separator(numbers):
    evens = []
    odds = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    return (evens, odds)