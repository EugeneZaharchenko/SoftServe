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

import tempfile
# to handle input
import sys
# module to check if the file exists
import os.path


class FindReplace:
    def __init__(self, path, str_find, str_replace=None):
# AttributeError никогда не должен будет зарайзится потому как если в методе file_existence не будет пути то уже райзится ошибка
        if not self.file_existence(path):
            raise AttributeError
        self.path = path
        self.str_find = str_find.lower()
        self.str_replace = str_replace
        self._count = 0

    @staticmethod
    def file_existence(path):
        """
        Func to check if the file exists
        :param path: path to file -> str
        :return: path to file -> str
        """
        if os.path.isfile(path):
            return path
        raise IOError

    def count(self, find):
        """
        Func to count frequency of the requested string
        :param find: string to find -> str
        :return: frequency of requested string in the given file -> int
        """
        _count = 0
        _find = find.lower()
        with open(self.path) as file:
            for line in file:
                _count += line.lower().count(_find)
        return _count

    def replace(self, find, rep):
        """
        Func to find and replace the requested string
        :param find: string to find -> str
        :param rep: optional string to find -> str
        :return: None
        """
        with open(self.path) as file:
            with tempfile.NamedTemporaryFile("w", delete=False) as tmp:
                for line in file:
                    tmp.write(line.replace(find, rep))
                tmp_name = tmp.name
        if tmp_name:
            os.remove(self.path)
            os.rename(tmp_name, self.path)

    # reload class magic method
    def __str__(self):
# вызов интерфейсных методов в '__str__'
        count = self.count(self.str_find)
        if self.str_replace:
            self.replace(self.str_find, self.str_replace)
            return "String {str_find} in given file was found {count} times.\n" \
                   "Requested string was replaced for {rep}.".format(str_find=self.str_find, count=count,
                                                                     rep=self.str_replace)
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
