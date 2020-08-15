def decorator(func):
    def inner(*args, **kwargs):
        print("entered decorator")
        result = func(*args, **kwargs)
        return result
    return inner

@decorator
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add)
    # add = decorator(add)
    # print(add)
    # add(1, 2) = decorator(add)(1,2)
    print(add(1, 2))
