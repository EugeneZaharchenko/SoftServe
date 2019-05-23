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
    def __init__(self, path):
        self._path = path
        self.tick_store = set()
        self._mode = self.mode_and_read()

    @staticmethod
    def validate(number):
        if len(number) != 6 or float(number) == 'Inf':
            raise ValueError("A lucky number can be 6 digits only")
        return int(number)
# выгрузка всех данных файла за раз
# использование интерфейсного метода в '__str__'
    def mode_and_read(self):
        """
        Func to set Moskow|Piter mode and to read numbers
        :return: Moskow|Piter mode -> str
        """
        with open(self._path) as file:
            lines = file.readlines()

            # read frst line in file to set mode
            _mode = lines[0].strip().lower()

            # read tickets' numbers in file
            [self.tick_store.add(line.strip()) for line in lines[1:]]
        if _mode == "piter":
            return _mode
        return "moskow"

    def happy(self, number):
        """
        Func to determine whether a ticket is lucky
        :param number: ticket's number -> str
        :return: number is lucky or not -> bool
        """
        if self._mode == "piter":
            _odd = sum([int(number[v]) for v in range(len(number)) if v % 2])
            _even = sum([int(number[v]) for v in range(len(number)) if not v % 2])
            if _odd == _even:
                return True
            return False

        _first = sum(map(int, number[:3]))
        _last = sum(map(int, number[3:]))
        if _first == _last:
            return True
        return False

    def count(self):
        """
        Func to count a quantity of lucky numbers
        :return: quantity of lucky numbers -> int
        """
        _count = 0
        for tick in self.tick_store:
            if self.happy(tick):
                _count += 1
        return _count

    # reload class magic method
    def __str__(self):
        _cnt = self.count()
        return "In the file {path} you entered there are {num} tickets." \
               " {cnt} are lucky with {mode} mode".format(path=self._path, num=len(self.tick_store),
                                                          mode=self._mode, cnt=_cnt)


def main():
    def file_existence(_path):
        """
        Func to check if the file exists
        :param _path: path to file -> str
        :return: path to file -> str
        """
        if os.path.isfile(_path):
            return _path
        raise IOError

    if len(sys.argv) == 1:
        print(__doc__)

    while True:
        try:
            # receive user's data
            path = input('Enter file path to determine Moskow/Peter mode of lucky number: ').strip()
            if file_existence(path):
                ticket = LuckyNumber(path)
        except IOError:
            print("The file doesn't exist")
            continue
        except ValueError:
            print("A lucky number can be of 6 digits only. Please, enter correct numbers")
            continue
        else:
            print(ticket)
        finally:
            repeat = input('Do you want to continue? (y/n): ')
            repeat.lower().strip()
            if repeat not in ('y' or 'yes'):
                break


if __name__ == "__main__":
    main()
