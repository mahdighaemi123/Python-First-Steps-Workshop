# https://quera.org/problemset/17675/

num_range = int(input())

def fibo(index):
    if index == 0:
        return 0

    if index == 1 or index == 2:
        return 1

    return fibo(index-1) + fibo(index-2)


def find_in_fibi(num):
    i = 1
    while 1:
        fibos = []
        fibos.append(fibo(i))
        i += 1

        if fibos[-1] == num:
            return True

        if fibos[-1] > num:
            return False


for i in range(1, num_range+1):
    if find_in_fibi(i):
        print("+", end="")
    else:
        print("-", end="")
