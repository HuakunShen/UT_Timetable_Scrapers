import itertools
import string
from multiprocessing import Pool
import matplotlib.pyplot as plt
import time


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    numbers = range(50)
    # no multiprocess
    # sum1 = 0
    # start_time = time.time()
    # for n in numbers:
    #     sum1 += fib(n)
    # end_time = time.time() - start_time

    # with multiprocess
    start_time = time.time()
    p = Pool()
    result = p.map(fib, numbers)
    sum2 = sum(result)
    p.close()
    p.join()
    end_time2 = time.time() - start_time
    print(end_time)
    print(end_time2)
    print(sum1)
    print(sum2)