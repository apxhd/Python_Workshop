#Program to make a decorator


def add_three(some_function):
    def wrapper(*args, **kwargs):
        x = some_function(*args, **kwargs)
        return some_function(x, 3)
    return wrapper


@add_three
def sum(a, b):
    return a+b

print(sum(2, 3))
