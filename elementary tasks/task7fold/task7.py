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
        if self.validate(limit) and self.range_check(limit):
            self.limit = int(limit)

        self.numbers_list = []

    def validate(self, val):
        if not str(val).isdigit():
            raise ValueError
        else:
            return val

    def range_check(self, val):
        if float(val) == 'Inf' or int(val) < 0:
            raise IndexError
        elif float(val) == 'NaN':
            raise ValueError
        else:
            self.limit = int(val)

    def count_limit(self):
        if self.limit == 0:
            return []
        else:
            self.numbers_list = [str(n) for n in range(self.limit) if n ** 2 < self.limit]
            return self.numbers_list

    def __str__(self):
        final_list = self.count_limit()
        if final_list == []:
            return "You entered {lim}. The answer is {zero}".format(lim=self.limit, zero=0)
        else:
            return "Sequence of numbers whose pow of 2 is less the {lim} is: {seq}".format(lim=self.limit,
                                                                                       seq=', '.join(final_list))


def main():

    if len(sys.argv[:]) == 1:
        print(__doc__)

    try:
        # creating instance of Number class with given arguments
        num = Number(sys.argv[1])
        print(num)
    except (ValueError, AttributeError):
        print("Wrong argument. It must be a positive NUMBER to limit the output")
    except IndexError:
        print("Wrong argument. Input a number in reasonable range to limit the output")


if __name__ == "__main__":
    main()
