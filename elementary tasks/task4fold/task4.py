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

# to handle input
import sys
import re
# module to check if the file exists
import os.path


class FindReplace:
    def __init__(self, path, str_find, str_replace=None):
        if self.file_existence(path):
            self.path = path
            self.str_find = str_find.lower()
            self.str_replace = str_replace
            self._count = 0
        else:
            raise AttributeError

    # check if the file exists
    def file_existence(self, path):
        if os.path.isfile(path):
            return path
        else:
            raise IOError

    def count(self, find):
        with open(self.path, 'r+', encoding='utf-8') as file:
            for line in file:
                line.rstrip('\n').lower()
                if find in line:
                    self._count += len(re.findall(find, line))
                else:
                    continue
        return self._count

    def replace(self, find, rep):
        with open(self.path, 'w+') as file:
            lines = file.readlines()

            for line in lines:
                if find in line.strip():
                    # str_find = self.str_find
                    newline = re.sub(find, rep, line)
                    file.write(newline)
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
    elif len(sys.argv) < 3:
        print('Wrong input. Enter parameters: path_to_file string_to_find')
    else:
        try:
            fr = FindReplace(*sys.argv[1:])
        except AttributeError as err:
            print("Incorrect file attribute. The whole error description is: {0}".format(err))
        except IOError:
            print("The file doesn't exist")
        else:
            print(fr)


if __name__ == "__main__":
    main()
