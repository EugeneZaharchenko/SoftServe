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
    def __init__(self, number, one_to_n, decs, hunds, thous):
        self.number = number
        self.units = one_to_n
        self.decs = decs
        self.hunds = hunds
        self.thousands = thous
        self.result_str = ""

    def unit_convert(self, num):
        """
        Func to convert units of number (0-10)
        :param num: Number to convert to string ->
        :return:
        """
        return self.units[num]

    # to convert digits 0-19
    def two_convert(self, num, string):
        if num in range(20):
            result = self.units[num]

        else:
            result = self.decs[int(string[0])]

            if string[1] != '0':
                result = '{0} {1}'.format(result, self.units[int(string[1])])

        return result

    # main convert func
    def convert(self, s_num):
        _len = len(s_num)
        _int_num = int(s_num)

        # using certain convert func for a certain number length
        if _len == 1:
            result = self.unit_convert(_int_num)
        elif _len == 2:
            result = self.two_convert(_int_num, s_num)
        elif _len == 3:
            result = self.hunds[int(s_num[0])]
            tail = s_num[-2:]
            if tail != '00':
                result = '{0} {1}'.format(result, self.convert(tail))
        elif _len in range(4, 7):

            # split number into head(first 3 digits) and tail(last 3)
            tail = self.convert(s_num[-3:])
            str_head = s_num[:-3]
            int_head = int(str_head)
            if int_head in range(1, 5):
                head = self.thousands[int_head]
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
                number = NumToWords(data, ONE_TO_NINETEEN, DECS, HUNDS, THOUSANDS)
            print("{}".format(number))
        finally:
            repeat = input('Would you like to continue? (y/n): ')
            repeat.lower().strip()
            if repeat not in ('y' or 'yes'):
                break


if __name__ == "__main__":
    main()
