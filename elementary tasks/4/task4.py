"""
Elementary Task #4

Файловый парсер
----------------

Программа имеет два режима:
1. Считать количество вхождений строки в текстовом файле.
2. Делать замену строки на другую в указанном файле
Программа должна принимать аргументы на вход при запуске:
<путь к файлу> <строка для подсчёта>
<путь к файлу> <строка для поиска> <строка для замены>

"""

import sys
import re


class FindReplace:
    def __init__(self, path, str_find, str_replace=None):
        self.path = path
        self.str_find = str_find.lower()
        self.str_replace = str_replace
        self._count = 0

    def count(self, find):
        find = find
        with open(self.path, 'r+', encoding='utf-8') as file:
            for line in file:
                line.rstrip('\n').lower()
                if find in line:
                    self._count += len(re.findall(find, line))
                else:
                    continue
        return self._count

    def replace(self, find, rep):
        with open(self.path, 'a+') as file:
            for line in file:
                if find in line:
                    file.write(line.replace(find, rep))
                else:
                    continue

    def __str__(self):
        count = self.count(sys.argv[2])
        if self.str_replace:
            self.replace(sys.argv[2], sys.argv[3])
            return "String {str_find} in given file was found {count} times.\n" \
                   "Requested string was replaced for {rep}.".format(str_find=self.str_find, count=count,
                                                                     rep=self.str_replace)
        else:
            return "String {str_find} in given file was found {count} times.".format(str_find=self.str_find,
                                                                                     count=count)


def main():

    if len(sys.argv) == 1:
        print(__doc__)
        exit()
    elif len(sys.argv) < 3:
        print('Enter parameters: path_to_file string_to_find')

    fr = FindReplace(*sys.argv[1:])
    print(fr)


if __name__ == "__main__":
    main()
