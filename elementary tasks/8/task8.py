import sys


def main():
    class Fibonacci:
        def __init__(self):
            self.i = 0
            self.x = 0
            self.y = 1
            self.F = [self.x, self.y]

        def next(self):
            self.i += 1
            return self.F[self.i - 1]  # return next # from list F

        def calculate(self, n):
            # use previously computed fibonachi numbers stored in list F
            l = len(self.F)
            x = self.F[l - 2]
            y = self.F[l - 1]
            newn = n - l
            # calculate new numbers if it does not exist in list
            for i in range(newn + 1):
                x, y = y, x + y
                self.F.append(y)
            return self.F[n]  # return nth # in Fibonacci series

        # def writeToFile(self, n, filename):
        #     filehandle = open(filename, 'a')  # append to file
        #     self.calculate(n)
        #     for j in range(n):
        #         filehandle.write(str(self.F[j]) + '\n')
        #     filehandle.close()


print()


if __name__ == "__main__":
    main()
