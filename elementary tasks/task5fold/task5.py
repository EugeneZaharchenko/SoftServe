"""
Elementary Task #5

Число в пропись
----------------

Нужно преобразовать целое число в прописной вариант: 12 – двенадцать.
Программа запускается через вызов главного класса с параметрами.

"""

import sys
from enum import Enum


units = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
tens = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
decimals = ['два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
hundreds =
thousands =
tens_thousands =
hundr_thousands =


class GenDigit(Enum):
    _units = {k:v for k,v in enumerate(units, start=1)}
    _tens = None
    _decimals = None
    _hundreds = None
    _thousands = None
    _tens_thousands = None
    _hundr_thousands = None


class NumToWords :
    def __init__(self, number):
        self.number = number
        self._digits = self.digit(number)

    @staticmethod
    def digit(num):
        _digits = []
        while len(str(num)) > 1:
            n, rem = divmod(num, 10)
            _digits.append(rem)
            num = n
        _digits.append(num)
        return _digits[::-1]

    def represent(self):



    # @property
    #
    # def __str__(self):
    #     # return '{name}: {area:g} cm'.format(name=self.name, area=self.area)
    #
    # def __repr__(self):
    #     # return self.area


def main():

    if len(sys.argv) == 1:
        print(__doc__)

    while True:
        try:
            data = input('Введите число: ').strip()
            if not all([s for s in data if s.isnumeric()]):
                raise ValueError
        except ValueError:
            print("Параметры заданы неверно. Задайте число")
            continue
        else:
            if data == "0":
                number = "ноль"
            else:
                number = NumToWords(data)
            print(number)
        finally:
            repeat = input('Хотите продолжить? (y/n): ')
            repeat.lower().strip()
            if repeat not in ('y' or 'yes'):
                break


if __name__ == "__main__":
    main()
