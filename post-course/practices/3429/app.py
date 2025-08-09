# https://quera.org/problemset/3429/

tempeture = int(input())

if tempeture < 0:
    print("Ice")
elif tempeture <= 100:
    print("Water")
else:
    print("Steam")