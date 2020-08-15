import time


class Timeit:
    def __init__(self, func):
        self.func = func
        self.initial = time.time()
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        final = time.time()
        print("total time it took is %s seconds" % (final - self.initial))
        return result


@Timeit
def test():
    for i in range(1000):
        print(i+1)

if __name__ == "__main__":
    test()
