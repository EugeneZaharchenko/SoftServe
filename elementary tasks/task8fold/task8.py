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
        if int(stop) < int(start):
            raise ValueError
        self.start = int(start)
        self.stop = int(stop)

    @staticmethod
    # lru_cache used to cash previously calculated values
    @lru_cache(maxsize=None)
    def gen_fib():
        """
        Fibonacci sequence generator
        :return: Fibonacci sequence ->
        """
        a, b = 0, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    # reload class magic methods
    def __str__(self):
        g = self.gen_fib()
        return ", ".join([str(next(g)) for _ in range(self.stop)])

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
