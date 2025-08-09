# Condition:
# We use conditions in programming to instruct the computer to execute a
# specific part of the program under certain circumstances.


# if elif and else
temp = 20

if temp <= 0:
    print("ice")

if 0 < temp < 100:
    print("water")

if temp >= 100:
    print("steam")


# one line condition
age = 21

if age >= 18:
    have_licence = "ok"
else:
    have_licence = "no"

have_licence = "ok" if age >= 18 else "no"
print("ok" if age >= 18 else "no")

# nested if else
num1 = 20
num2 = 22

if num1 % 2 == 0:
    if num2 % 2 == 0:
        print("both even")
    else:
        print("num 1 even", "num 2 odd")
else:
    if num2 % 2 == 0:
        print("num 1 odd", "num 2 even")
    else:
        print("both odd")
