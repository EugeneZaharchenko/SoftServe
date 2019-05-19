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

    def mode_and_read(self):

        with open(self._path) as file:
            lines = file.readlines()

            # read frst line if file to set mode
            _mode = lines[0].strip().lower()

            [self.tick_store.add(line.strip()) for line in lines[1:]]
        if _mode == "piter":
            return _mode
        return "moskow"

    def happy(self, number):
        if self._mode == "piter":
            odd = sum([int(number[v]) for v in range(len(number)) if v % 2])
            even = sum([int(number[v]) for v in range(len(number)) if not v % 2])
            if odd == even:
                return True
            return False

        first = sum(map(int, number[:3]))
        last = sum(map(int, number[3:]))
        if first == last:
            return True
        return False

    def count(self):
        _count = 0
        for tick in self.tick_store:
            if self.happy(tick):
                _count += 1
        return _count

    def __str__(self):
        _cnt = self.count()
        return "In the file {path} you entered there are {num} tickets." \
               " {cnt} are lucky with {mode} mode".format(path=self._path, num=len(self.tick_store),
                                                          mode=self._mode, cnt=_cnt)


def main():
    # check if the file exists
    def file_existence(_path):
        if os.path.isfile(_path):
            return _path
        raise IOError

    if len(sys.argv) == 1:
        print(__doc__)

    while True:
        try:
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
            repeat = input('Хотите продолжить? (y/n): ')
            repeat.lower().strip()
            if repeat not in ('y' or 'yes'):
                break


if __name__ == "__main__":
    main()
