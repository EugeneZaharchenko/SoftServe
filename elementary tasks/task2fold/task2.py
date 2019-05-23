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
# слишк много приведений типов в valid, можно один раз привести к float и просто проверить
import sys


class Envelope:
    def __init__(self, width, height):
        self.width, self.height = self.valid(width, height)

    @staticmethod
    def valid(width, height):
        if not (str(width).isdigit() or str(height).isdigit()):
            return ValueError
        if float(width) <= 0 or float(height) <= 0:
            raise ValueError
        return float(width), float(height)

    # reload class magic methods
    def __lt__(self, other):
        return (self.width < other.width) & (self.height < other.height)

    def __gt__(self, other):
        return (self.width > other.width) & (self.height > other.height)


def main():
    if len(sys.argv) == 1:
        print(__doc__)

    def compare(obj1, obj2):
        if ((obj1.width > obj2.width) & (obj1.height > obj2.height)
                & (obj1.height > obj2.width) & (obj1.width > obj2.height)):
            print('The second envelope may be put to the first in any position.')
        elif obj1 > obj2:
            print('The second envelope may be put to the first, but if the second is not reversed.')
        else:
            print('No way to put the second envelope into the first!')

    while True:
        try:
            # receive user's data
            width1 = input('Input a width of first envelope: ')
            height1 = input('Input a height of first envelope: ')
            width2 = input('Input a width of second envelope: ')
            height2 = input('Input a height of second envelope: ')

            # create two instances of Envelope class with given arguments
            envelope1 = Envelope(width1, height1)
            envelope2 = Envelope(width2, height2)

        except IndexError:
            print("Wrong parameters. Please, input envelopes' width and height.")
            continue
        except ValueError:
            print("Given parameters are wrong. Please, input envelopes' width and height in numbers.")
            continue
        else:
            compare(envelope1, envelope2)
        finally:
            again = input('Do you want to continue? (y/n): ')
            again.lower().strip()
            if again not in ('y', 'yes'):
                break


if __name__ == "__main__":
    main()
