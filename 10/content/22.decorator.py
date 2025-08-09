# decorator:
# A decorator in Python is essentially wrapping a function inside another function to add extra behavior before or after the original function runs
# without modifying the original function’s code directly.
print_data = ....


@print_data
def sum(a, b):
    return a + b

@print_data
def divide(a, b):
    return a / b


def wrapper(a, b):
    print(a,b)
    # print("🚀 Something before the function runs.")
    result = sum(a, b)
    # print("✅ Something after the function runs.")
    return result

sum(1,2)
wrapper(1,2)

sum = wrapper









print(sum(1, 2))
print(wrapper(1, 2))








# now using decorator

def my_decorator(func):

    def wrapper(a, b):
        print("🚀 Something before the function runs.")
        sum(a, b)  # calling the original function
        print("✅ Something after the function runs.")

    return wrapper


@my_decorator
def sum(a, b):
    return a + b

sum(1,2)



@my_decorator
def sum(a, b):
    return a + b


print(sum(1, 2))
