"""
Elementary Task 7

Sequence of numbers
----------------

The program outputs a sequence of comma separated natural numbers where their square degree is less than given n.
The program runs through call of main class with parameters.
"""

import sys


class Number:
    def __init__(self, limit):
        if self.validate(limit):
            self.limit = self.range_check(limit)
        self.numbers_list = []

    @staticmethod
    def validate(val):
        """
        Func to validate if the input data is correct
        :param val: entered data ->  str
        :return: data -> str
        """
        if not str(val).isdigit():
            raise ValueError
        return val

    @staticmethod
    def range_check(val):
        """
        Func to check if the count range is correct
        :param val: max value of range -> str
        :return: max value of range -> int
        """
        if float(val) == 'Inf' or int(val) < 0:
            raise IndexError
        return int(val)

    def count_limit(self):
        """
        Func to calculate numbers which square degree is less than given limit
        :return: numbers which square degree is less than given -> list
        """
        self.numbers_list = [str(n) for n in range(1, self.limit) if n ** 2 < self.limit]
        return self.numbers_list

    # reload class magic method
    def __str__(self):
        final_list = self.count_limit()
        if not final_list:
            return "You entered {lim}. The answer is {zero}".format(lim=self.limit, zero=0)
        return "Sequence of numbers whose pow of 2 is less the {lim} is: {seq}".format(lim=self.limit,
                                                                                       seq=', '.join(final_list))


def main():
    if len(sys.argv) == 1:
        print(__doc__)

    try:
        # receive user's data
        n = sys.argv[1]
        # creating instance of Number class with given arguments
        num = Number(n)
    except (ValueError, AttributeError):
        print("Wrong argument. It must be a positive NUMBER to limit the output")
    except IndexError:
        print("Wrong argument. Input a number in reasonable range to limit the output")
    else:
        print(num)


if __name__ == "__main__":
    main()
