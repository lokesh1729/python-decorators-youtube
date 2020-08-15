import functools
import time


def timeit(func):
    """
    timeit decorator
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        before_calling = time.time()
        result = func(*args, **kwargs)
        after_calling = time.time()
        print("function %s has took %s seconds" % (func.__name__, (after_calling - before_calling)))
        return result
    return wrapper


def test_timeit_without_decorator():
    """
    testing timeit function
    """
    for i in range(100):
        print(i+1)


@timeit
def test_timeit_with_decorator():
    """
    testing timeit function
    """
    for i in range(100):
        print(i+1)


if __name__ == "__main__":
    print("without decorator")
    print(test_timeit_without_decorator)
    print(test_timeit_without_decorator.__module__)
    print(test_timeit_without_decorator.__name__)
    print(test_timeit_without_decorator.__doc__)
    print("with decorator")
    print(test_timeit_with_decorator)
    print(test_timeit_with_decorator.__module__)
    print(test_timeit_with_decorator.__name__)
    print(test_timeit_with_decorator.__doc__)
