def decorator(*dargs, **dkwargs):
    def wrapped(func):
        def inner(*args, **kwargs):
            print("entered decorator")
            result = func(*args, **kwargs)
            return result
        return inner
    return wrapped
