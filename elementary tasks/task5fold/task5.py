"""
Elementary Task #5

Число в пропись
----------------

Нужно преобразовать целое число в прописной вариант: 12 – двенадцать.
Программа запускается через вызов главного класса с параметрами.

"""

import sys
from num2words import num2words


def main():

    if len(sys.argv[:]) == 1:
        print(__doc__)

    number = int(input('Введите целое число: '))
    print(num2words(number, lang='ru'))


if __name__ == "__main__":
    main()
