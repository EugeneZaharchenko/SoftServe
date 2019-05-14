"""
Elementary Task #7

Числовая последовательность
----------------

Программа выводит ряд натуральных чисел через запятую, квадрат которых меньше заданного n.
Программа запускается через вызов главного класса с параметрами.
"""

import sys


class Number:
    def __init__(self, limit):
        if int(limit) < 0:
            raise ValueError
        else:
            self.limit = int(limit)
        self.numbers_list = []
        # if not all([s for s in sys[1:] if s.isnumeric()]):
        #     raise ValueError
        # else:
        #     self.limit = int(limit)
        #     self.numbers_list = []
#     num = int(input('Введите заданное граничное число: '))

    def count_limit(self):
        self.numbers_list = [str(n) for n in range(self.limit) if n ** 2 < self.limit]

    def __str__(self):
        self.count_limit()
        return "Sequence of numbers whose pow of 2 is less the {lim} is: {seq}".format(lim=self.limit,
                                                                                      seq=', '.join(self.numbers_list))


def main():

    if len(sys.argv[:]) == 1:
        print(__doc__)

    try:
        # creating instance of Number class with given arguments
        num = Number(sys.argv[1])
        print(num)
        exit()
    except ValueError:
        print("Wrong argument. It must be a positive NUMBER to limit the output")
    except IndexError:
        print("Wrong argument. Give a number to limit the output")


if __name__ == "__main__":
    main()
