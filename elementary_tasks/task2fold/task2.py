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
        else:
            self.width = float(width.strip())
            self.height = float(height.strip())

    def __lt__(self, other):
        return (self.width < other.width) & (self.height < other.height)

    def __gt__(self, other):
        return (self.width > other.width) & (self.height > other.height)


def main():
    if len(sys.argv) == 1:
        print(__doc__)

    while True:
        try:
            width1 = input('Введите ширину первого конверта: ')
            height1 = input('Введите высоту первого конверта: ')
            width2 = input('Введите ширину второго конверта: ')
            height2 = input('Введите высоту второго конверта: ')

            # create two instances of Envelope class with given arguments
            env1 = Envelope(width1, height1)
            env2 = Envelope(width2, height2)

        except IndexError:
            print("Неверные параметры. Задайте ширину и высоту конвертов")
            continue
        except ValueError:
            print("Параметры заданы неверно. Задайте численно ширину и высоту конвертов")
            continue
        else:
            if env1 > env2:
                print('Второй конверт можно вложить в первый, если второй конверт не переворачивать')
            elif ((env1.width > env2.width) & (env1.height > env2.height)
                & (env1.height > env2.width) & (env1.width > env2.height)):
                print('Второй конверт можно вложить в первый в любом положении')
            else:
                print('Второй конверт вложить не удастся!')
        finally:
            again = input('Хотите продолжить? (y/n): ')
            again.lower().strip()
            if again not in ('y', 'yes'):
                break


if __name__ == "__main__":
    main()
