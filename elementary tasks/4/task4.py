import sys
'''Прога должна принимать аргументы:
    1. <путь к файлу><строка поиска>
    2. <путь к файлу><строка поиска><строка замены>
'''


class FindReplace:
    def __init__(self, path, str_count, str_replace=None):
        self.path = path
        self.string_count = str_count
        self.string_replace = str_replace

    def count(self):
        count = 0
        with open(self.path, 'r') as file:
            for line in file:
                line.strip()
                if self.string_count in line:

                    count += 1
        return count
                # file.readline
            #     strs = line.split('\n')
            #     str_count += len(strs)
        # return "Число вхождений строки: ", str_count)

    def replace(self):
        with open(self.path, 'wt') as file:
            for line in file:
                line.replace(self.string_count, self.string_replace)


def main():
    file_name = input("Введите имя файла: ")

    # with open(file_name, 'r') as f:
    #     for line in f:
    #         strs = line.split()
    #         str_count += len(strs)
    # print("Число вхождений строки: ", str_count)

    # with open(file_name, 'wt') as f:
    #     for line in f:
    #         line.replace(old_str, new_str)


if __name__ == "__main__":
    main()
