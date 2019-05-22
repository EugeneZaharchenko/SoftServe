"""
Elementary Task #1

Chess-board
---------------

The script aimed to print chess-board with given height and width parameters:
*  *  *  *  *  *
  *  *  *  *  *  *
*  *  *  *  *  *
  *  *  *  *  *  *
The program runs through main class call with parameters.
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
        # receive user's data
        chess_print = Chess(sys.argv[1], sys.argv[2])
        print(chess_print)
    except IndexError:
        print("Wrong parameters. Please, input row quantity and their length")


if __name__ == "__main__":
    main()
