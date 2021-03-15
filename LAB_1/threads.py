import threading
from datetime import datetime
from functools import wraps


def timer_dec(self, cell_func):
    @wraps(cell_func)
    def wraper(*args, **kwargs):
        START = datetime.now()
        cell_func(*args, **kwargs)
        END = datetime.now()
        print(f'{END - START}- время исполнения')

    return wraper


class Sorter(threading.Thread):
    def __init__(self, array, sort_way):
        threading.Thread.__init__(self)
        self.array = array
        self.sort_way = sort_way
        self.param_dict = {'bubble': self.bSort, 'sell': self.sel_sort, 'insert': self.insertion}
        print(self.sort_way)
        print("Initialized thread" + str(self))

    def run(self):
        START = datetime.now()
        self.param_dict[self.sort_way]()
        END = datetime.now()
        print(f'{END - START}- время исполнения {self.sort_way}')
        # print(param_dict[self.sort_way]())

    def bSort(self):
        length = len(self.array)
        for i in range(length):
            print(i)
            for j in range(0, length - i - 1):
                if self.array[j] > self.array[j + 1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = temp
        return 'b_sort pass'

    def sel_sort(self):
        for i in range(len(self.array) - 1):
            print(i)
            m = i
            j = i + 1
            while j < len(self.array):
                if self.array[j] < self.array[m]:
                    m = j
                j = j + 1
            self.array[i], self.array[m] = self.array[m], self.array[i]
        return 'sel_sort pass'

    def insertion(self):
        for i in range(len(self.array)):
            print(i)
            j = i - 1
            key = self.array[i]
            while self.array[j] > key and j >= 0:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        return 'incertion pass'
