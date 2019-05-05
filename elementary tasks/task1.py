import sys


class Chess:
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)

    row = '* '

    def print(self):
        if self.height == 1:
            print(self.row * self.width)
        else:
            row_reversed = self.row[::-1]
            half_height = self.height // 2
            for i in range(half_height):
                print(self.row * self.width, row_reversed * self.width, sep='\n')
            if self.height % 2:
                print(self.row * self.width)


def main():
    try:
        chess_print = Chess(sys.argv[1], sys.argv[2]).print()
    except IndexError:
        print("Неверные параметры. Задайте высоту и ширину")

    if len(sys.argv[1:]) == 0:
        print("""Задайте высоту и ширину для вывода шахматной доски с заданными размерами,\
        по принципу
        *  *  *  *  *  *
            *  *  *  *  *  *
            """)


if __name__ == "__main__":
    main()
