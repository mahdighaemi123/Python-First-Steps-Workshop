# try-except:
# syntax for handling errors in try scoop

# when any error happend in try scoop
# expect scoop codes will run
try:
    print(1)    # run
    print(1/0)  # error
    print(2)    # not run
except:
    print("error happend")


try:
    b = 0
    if b == 0:
        raise SystemError("11111") # creating error

except Exception: # specify type of error catch
    print("error happend")


try:

    list = []
    list[20]

except ZeroDivisionError as error: # only catching zero division error so index error will crash app
    print(error)
