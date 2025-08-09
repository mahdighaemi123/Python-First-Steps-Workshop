# https://quera.org/problemset/10230/

nums = input().split()

num1 = int(nums[0])
num2 = int(nums[1])
num3 = int(nums[2])

if sum([num1, num2, num3]) == 180 and num1 * num2 * num3 > 0:
    print("Yes")
else:
    print("No")