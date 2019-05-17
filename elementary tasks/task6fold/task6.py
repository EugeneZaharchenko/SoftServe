"""
Elementary Task 6

Счастливые билеты
----------------

Номер билета - шестизначное число. Программа может посчитать количество счастливых билетов.
Для выбора алгоритма подсчёта читается текстовый файл. Путь к текстовому файлу задаётся в консоли
после запуска программы.
Индикаторы алгоритмов:
    1 - слово 'Moskow'
    2 - слово 'Piter'
После задания всех необходимых параметров, программа в консоль должна вывести
количество счастливых билетов для указанного способа подсчёта.

"""
import sys
import os.path


class LuckyNumber:
    def __init__(self, path, number):
        if self.validate(number):
            self.number = int(number)
        self.path = path
        self._mode = self.mode(self)

    @staticmethod
    def validate(number):
        if not str(number).isdigit() or len(number) != 6:
            raise ValueError("A lucky number can be of 6 digits only")
        elif float(number) == 'Inf' or float(number) == 'NaN':
            raise ValueError
        elif int(number) == 0:
            return 0
        return number

    @staticmethod
    def mode(self):
        with open(self.path) as file:
            for line in file:
                _mode = line.lower()
        if _mode in ('moskow', 'piter'):
            return _mode
        return 'moskow'

    def count(self, number):
        if self._mode == 'piter':
            odd = sum([v for v in number if int(v) % 2])
            even = sum([v for v in number if not int(v) % 2])
            if odd == even:
                return True
            return False

        first = sum(map(int, number[:3]))
        last = sum(map(int, number[3:]))
        if first == last:
            return True
        return False
        # else:
        #     for i in range(int(number), 999999):
        #         i = str(i)
        #         a, b = sum(map(int, i[:3])), sum(map(int, i[3:]))
        #         if a == b:
        #             print("Next Lucky Ticket: " + i)
        #             break

    def __str__(self):
        if self.count(sys.argv[1]):
            return "Horrah! You entered {num} and you've got a lucky number!".format(num=self.number)
        return "The number {num} you entered isn't a lucky. Maybe try again.".format(num=self.number)


def main():
    # check if the file exists
    def file_existence(path):
        if os.path.isfile(path):
            return path
        raise IOError

    if len(sys.argv) == 1:
        print(__doc__)
    # elif len(sys.argv) < 3:
    #     print('Wrong input. Enter parameters: path_to_file string_to_find')

        # except AttributeError as err:
        #     print("Incorrect file attribute. The whole error description is: {0}".format(err))
        # else:
        #     print(fr)

    while True:
        ticket = None
        try:
            path = input('Enter file path to determine Moskow/Peter mode of lucky number: ').strip()
            # path = 'mode.txt'
            num = input("Please enter you number: ")
            if file_existence(path):
                ticket = LuckyNumber(path, num)
        except IOError:
            print("The file doesn't exist")
            continue
        except ValueError:
            print("A lucky number can be of 6 digits only. Please, enter correct numbers")
            continue
        else:
            print(ticket)
        finally:
            repeat = input('Хотите продолжить? (y/n): ')
            repeat.lower().strip()
            if repeat not in ('y' or 'yes'):
                break


if __name__ == "__main__":
    main()