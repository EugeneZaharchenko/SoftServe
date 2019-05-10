import sys


class Chess:
    """
    This is a class for printing stings in special 'chess' manner.

    Attributes:
        height (int): The quantity of printed strings.
        width (int): The width of each printed string.
    """
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)

    row_pattern = '* '

    def __str__(self):
        """
        The function to print data of Chess class.

        Parameters:
            self (Chess): The instance of Chess class to be printed.

        Returns:
            Chess: A string formatted in special 'chess' way.
        """
        if self.height == 1:
            return '{}'.format(self.row_pattern * self.width)
        else:
            row_reversed = self.row_pattern[::-1]
            half_height = self.height // 2
            for i in range(half_height):
                return '{0} \n {1}'.format(self.row_pattern * self.width, row_reversed * self.width)
            # if self.height % 2:
            #     return '\n {0}'.format(self.row_pattern * self.width)


def main():
    instructions = """
        Вывести шахматную доску с заданными размерами высоты и ширины, по принципу
        *  *  *  *  *  *
          *  *  *  *  *  *
        *  *  *  *  *  *
          *  *  *  *  *  *
    """
    try:
        chess_print = Chess(sys.argv[1], sys.argv[2])
        print(chess_print)
        exit()
    except IndexError:
        print("Неверные параметры. Задайте количество строк и их длину")

    if len(sys.argv[:]) == 1:
        print(instructions)


if __name__ == "__main__":
    main()
