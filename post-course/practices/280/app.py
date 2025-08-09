# https://quera.org/problemset/280/

a = int(input())
b = int(input())
c = int(input())

nums = [a, b, c]
nums.sort()

if nums[2]**2 == nums[0] ** 2 + nums[1] ** 2:
    print("YES")
else:
    print("NO")
