import sys


def main():
    from num2words import num2words
    number = int(input('Введите целое число: '))
    print(num2words(number, lang='ru'))


if __name__ == "__main__":
    main()

