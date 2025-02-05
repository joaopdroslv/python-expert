import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print('Time taken: ', total)
        return rv
    
    return wrapper


@timer
def count_to_1_mil():
    for _ in range(1000000):
        pass


@timer
def test():
    time.sleep(5)


# count_to_1_mil()
test()