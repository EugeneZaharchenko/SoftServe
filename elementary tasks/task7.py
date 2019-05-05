import sys


def main():
    num = int(input('Введите заданное граничное число: '))
    list = [n for n in range(num) if n ** 2 < num]
    for s in list:
        print(s, end=',')


if __name__ == "__main__":
    main()
