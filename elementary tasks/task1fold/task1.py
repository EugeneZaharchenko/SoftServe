"""
Elementary Task #1

Шахматная доска
---------------

Вывести шахматную доску с заданными размерами высоты и ширины, по принципу:
*  *  *  *  *  *
  *  *  *  *  *  *
*  *  *  *  *  *
  *  *  *  *  *  *
Программа запускается через вызов главного класса с параметрами.
"""
import sys


class Chess:
    """
    This is a class for printing stings in special 'chess' manner.

    Attributes:
        height (int): The quantity of printed strings.
        width (int): The width of each printed string.
    """
    _sign = '*'
    _space = ' '

    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)

    def __str__(self):
        """
        The function to print data of Chess class.

        Parameters:
            self (Chess): The instance of Chess class to be printed.

        Returns:
            Chess: A string formatted in special 'chess' way.
        """
        even_row = (self._sign + self._space) * self.width
        odd_row = self._space + even_row

        # using list generator to make strings which will be printed
        return "\n".join([odd_row if h % 2 else even_row for h in range(self.height)])

    def __repr__(self):
        return self.__str__()


def main():
    if len(sys.argv) == 1:
        print(__doc__)
        return

    try:
        chess_print = Chess(sys.argv[1], sys.argv[2])
        print(chess_print)
        exit()
    except IndexError:
        print("Неверные параметры. Задайте количество строк и их длину")


if __name__ == "__main__":
    main()
