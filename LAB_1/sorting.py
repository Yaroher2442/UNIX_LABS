from random import randint
from numba import njit
from functools import wraps
from datetime import datetime
# from threads import Sorter

RAND_MAX = 1000


def timer_dec(cell_func):
    @wraps(cell_func)
    def wraper(*args, **kwargs):
        START = datetime.now()
        cell_func(*args, **kwargs)
        END = datetime.now()
        print(f'{END - START}- время исполнения')
    return wraper

ls = [randint(0, RAND_MAX) for i in range(100000)]

@timer_dec
@njit
def bSort(ls):
    length = len(ls)
    for i in range(length):
        print(i)
        for j in range(0, length - i - 1):
            if ls[j] > ls[j + 1]:
                temp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = temp
    return 'b_sort pass'

def main():
    # START = datetime.now()
    ls = [randint(0, RAND_MAX) for i in range(100000)]
    bSort(ls)
    # modes = ['bubble', 'sell', 'insert']
    # wrkrs = []
    # for mode in modes:
    #     worker = Sorter(ls.copy(), mode)
    #     worker.setDaemon(True)
    #     worker.start()
    #     wrkrs.append(worker)
    # for worker in wrkrs:
    #     worker.join()


if __name__ == '__main__':
    main()
