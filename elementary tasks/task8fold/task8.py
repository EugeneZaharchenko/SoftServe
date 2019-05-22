"""
Elementary Task 8

Fibonacci sequence for a certain range
----------------

The program lets to output all Fibonacci numbers, which are in given range.
The range is given with 2 arguments during the main class call.
Fibonacci numbers are comma separated in output and sorted by asc.
"""

import sys
from functools import lru_cache


class Fibonacci:
    def __init__(self, start, stop):
        self.start, self.stop = self.validate(start, stop)

    @staticmethod
    def validate(start, stop):
        if int(stop) > 0 and int(stop) < int(start):
            raise ValueError
        if int(stop) < 0 and int(stop) > int(start):
            raise ValueError
        return int(start), int(stop)

    @staticmethod
    # lru_cache used to cash previously calculated values
    @lru_cache(maxsize=128)
    def gen_fib():
        """
        Fibonacci sequence generator
        :return: Fibonacci sequence -> iterator
        """
        a, b = 0, 1

        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    @staticmethod
    @lru_cache(maxsize=128)
    def gen_fib_neg():
        """
        Fibonacci sequence generator for negative numbers
        :return: Fibonacci sequence -> iterator
        """
        a, b = 0, 1

        yield a
        yield b
        while True:
            a, b = b, a - b
            yield b

    def fib_list(self):
        """
        Func to form Fibonacci list
        :return: list of Fibonacci numbers -> list
        """
        if self.stop < 0:
            g = self.gen_fib_neg()
            return [next(g) for _ in range(self.start, self.stop, -1)]
        g = self.gen_fib()
        return [next(g) for _ in range(self.stop)]

    # reload class magic methods
    def __str__(self):
        f_list = self.fib_list()
        if self.stop < 0:
            return ", ".join([str(s) for s in f_list if self.stop <= s <= self.start])
        return ", ".join([str(s) for s in f_list if self.start <= s <= self.stop])

    def __repr__(self):
        return self.__str__()


def main():
    if len(sys.argv) == 1:
        print(__doc__)

    try:
        # receive user's data
        start, stop = sys.argv[1], sys.argv[2]
        # creating instance of Fibonacci class in certain range which is given as arguments
        fib = Fibonacci(start, stop)
    except ValueError:
        print("Wrong arguments. Give start and stop values where stop is bigger (start < stop)")
    except IndexError:
        print("Wrong arguments. Must be 2 parameters: start, stop (start < stop)")
    else:
        print("Fibonacci sequence for a given range {start}-{stop} is: {seq}".format(start=start, stop=stop,
                                                                                     seq=fib))


if __name__ == "__main__":
    main()
