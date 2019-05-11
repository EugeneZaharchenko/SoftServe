from num2words import num2words
import sys


def main():

    number = int(input('Введите целое число: '))
    print(num2words(number, lang='ru'))


if __name__ == "__main__":
    main()
