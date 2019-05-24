"""
Elementary Task #5

Число в пропись
----------------

Нужно преобразовать целое число в прописной вариант: 12 – двенадцать.
Программа запускается через вызов главного класса с параметрами.
"""

import sys


ONE_TO_NINETEEN = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
                   'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
                   'восемнадцать', 'девятнадцать')

DECS = ('', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
        'девяносто')

HUNDS = ('', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот')

THOUSANDS = ('', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи')


class NumToWords:
    def __init__(self, number):
        self.number = self.validate(number)
        self.result_str = ""

    @staticmethod
    def validate(val):
        """
        Func to validate if the input data is correct
        """
        if not str(val).isdigit():
            raise ValueError
        return val

    @staticmethod
    def unit_convert(num):
        """
        Func to convert units between (0-10)
        """
        return ONE_TO_NINETEEN[num]

    @staticmethod
    def two_convert(num, string):
        """
        Func to convert digits 0-19 or tens
        """
        if num in range(20):
            result = ONE_TO_NINETEEN[num]

        else:
            result = DECS[int(string[0])]

            if string[1] != '0':
                result = '{0} {1}'.format(result, ONE_TO_NINETEEN[int(string[1])])

        return result

    def convert(self, s_num):
        """
        Main convert func
        """
        _len = len(s_num)
        _int_num = int(s_num)

        # using certain convert func for a certain number length
        if _len == 1:
            result = self.unit_convert(_int_num)
        elif _len == 2:
            result = self.two_convert(_int_num, s_num)
        elif _len == 3:
            result = HUNDS[int(s_num[0])]
            tail = s_num[-2:]
            if tail != '00':
                result = '{0} {1}'.format(result, self.convert(tail))
        elif _len in range(4, 7):

            # split number into head(first 3 digits) and tail(last 3)
            tail = self.convert(s_num[-3:])
            str_head = s_num[:-3]
            int_head = int(str_head)
            if int_head in range(1, 5):
                head = THOUSANDS[int_head]
            else:
                head = '{0} {1}'.format(self.convert(str_head), "тысяч")

            result = '{0} {1}'.format(head, tail)

        else:
            result = ''
        self.result_str = result.strip()
        return self.result_str

    # reload magic methods
    def __str__(self):
        self.convert(self.number)
        return self.result_str

    def __repr__(self):
        return self.__str__()


def main():
    if len(sys.argv) == 1:
        print(__doc__)

    while True:
        try:
            # receive user's data
            data = input('Input number to print: ').strip()
            if not all([s for s in data if s.isnumeric()]) or int(data) < 0:
                raise ValueError
        except ValueError:
            print("Wrong parameters. Give a positive number")
            continue
        else:
            if data == "0":
                number = "zero"
            else:
                number = NumToWords(data)
            print("{}".format(number))
        finally:
            repeat = input('Would you like to continue? (y/n): ')
            repeat.lower().strip()
            if repeat not in ('y' or 'yes'):
                break


if __name__ == "__main__":
    main()
