"""
Elementary Task #2

Анализ конвертов
----------------

Есть два конверта со сторонами (a,b) и (c,d) определить, можно ли один конверт вложить в другой.
Программа должна обрабатывать ввод чисел с плавающей точкой.

Программа спрашивает у пользователя размеры конвертов по одному параметру за раз.
После каждого подсчёта программа спрашивает у пользователя хочет ли он продолжить.
Если пользователь ответит “y” или “yes” (без учёта регистра), программа продолжает работу сначала,
в противном случае – завершает выполнение.
"""

import sys


class Envelope:
    def __init__(self, width, height):
        if float(width) or float(height) <= 0:
            raise ValueError
        self.width = float(width.strip())
        self.height = float(height.strip())

    # reload class magic methods
    def __lt__(self, other):
        return (self.width < other.width) & (self.height < other.height)

    def __gt__(self, other):
        return (self.width > other.width) & (self.height > other.height)


def main():
    if len(sys.argv) == 1:
        print(__doc__)

    while True:
        try:
            # receive user's data
            width1 = input('Input a width of first envelope: ')
            height1 = input('Input a height of first envelope: ')
            width2 = input('Input a width of second envelope: ')
            height2 = input('Input a height of second envelope: ')

            # create two instances of Envelope class with given arguments
            env1 = Envelope(width1, height1)
            env2 = Envelope(width2, height2)

        except IndexError:
            print("Wrong parameters. Please, input envelopes' width and height.")
            continue
        except ValueError:
            print("Given parameters are wrong. Please, input envelopes' width and height in numbers.")
            continue
        else:
            if ((env1.width > env2.width) & (env1.height > env2.height)
                    & (env1.height > env2.width) & (env1.width > env2.height)):
                print('The second envelope may be put to the first in any position.')
            elif env1 > env2:
                print('The second envelope may be put to the first, but if the second is not reversed.')
            else:
                print('No way to put the second envelope into the first!')
        finally:
            again = input('Do you want to continue? (y/n): ')
            again.lower().strip()
            if again not in ('y', 'yes'):
                break


if __name__ == "__main__":
    main()
