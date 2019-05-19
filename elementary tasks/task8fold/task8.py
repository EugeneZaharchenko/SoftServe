"""
Elementary Task 8

Fibonacci sequence for a certain range
----------------

The program lets to output all Fibonacci numbers, which are in given range.
The range is given with 2 arguments during the main class call.
Fibonacci numbers are comma separated in output and sorted by asc.

"""

import sys


class Fibonacci:
    def __init__(self, start, stop):
        if int(stop) > int(start):
            self.start = int(start)
            self.stop = int(stop)
            self.fibs = []
        else:
            raise ValueError

    @staticmethod
    def fib_seq(self):
        _fib_l = list(map(lambda x, f=lambda x, f: (f(x - 1, f)
                            + f(x - 2, f)) if x > 1 else 1: f(x, f), range(self.start, self.stop)))
        return _fib_l

    # print("{}".format(', '.join(fib_seq(2, b))))

    # def fib_seq(self):
    #     _start, _stop = self.start, self.stop
    #     return list(map(lambda x, f=lambda x, f: (f(x - 1, f)
    #                     + f(x - 2, f)) if x > 1 else 1: f(x, f), range(_start, _stop)))

    def __str__(self):
        return "Fib {}".format(", ".join([str(i) for i in self.fib_seq(self) if int(i) <= self.stop]))

    # def __str__(self):
    #     # _str = fib_seq()
    #     return "Fibonacci sequence for a given range {start}-{stop} is: {seq}".format(start=self.start, stop=self.stop,
    #                                                                                   seq=", ".join(self.fib()))
    #                                                                                   # seq=" ".join(self.fib_seq(self)))


def main():

    if len(sys.argv) == 1:
        print(__doc__)

    try:
        # creating instance of Fibonacci class in certain range which is given as arguments
        fib = Fibonacci(sys.argv[1], sys.argv[2])
    except ValueError:
        print("Wrong arguments. Give start and stop values where stop is bigger (start < stop)")
    except IndexError:
        print("Wrong arguments. Must be 2 parameters: start, stop (start < stop)")
        print(fib)


if __name__ == "__main__":
    main()
