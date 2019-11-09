"""
Fahrenheit convertion

Программа спрашивает у пользователя в каком формате будет задана температура.
Производит перевод указанных значений в другую систему измерения и выводит сообщение с ответом.
"""

import sys


def fahr(t):
    return t * 1.8 + 32


def celc(t):
    return (t - 32) / 1.8


def main():
    if len(sys.argv) == 1:
        print(__doc__)

    while True:
        try:
            system = input('Введите систему исчисления: fahr/celc\n')
            temp = input('Введите температуру: ')

            if not temp.isdigit():
                raise ValueError

            if system == 'fahr':
                abs_zero = -459
            elif system == 'celc':
                abs_zero = -273
            else:
                print("Неверно задана единица измерения")

            if float(temp) <= abs_zero:
                raise IndexError

            if system == 'fahr':
                print("{:.3f} градусов Цельсия".format(celc(float(temp))))
            else:
                print("{:.3f} градусов Фаренгейта".format(fahr(float(temp))))

        except ValueError:
            print("Неверные параметры. Задайте единицы измерения и численное значение температуры")
            continue
        except IndexError:
            print("Заданная температура ниже абсолютного нуля. Ничто вас не спасет!")
            continue
        finally:
            again = input('Хотите продолжить? (y/n): ')
            again.lower().strip()
            if again not in ('y', 'yes'):
                break


if __name__ == "__main__":
    main()
