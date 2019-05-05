import sys
'''Прога должна принимать аргументы:
    1. <путь к файлу><строка поиска>
    2. <путь к файлу><строка поиска><строка замены>
'''


def main():
    file_name = input("Введите имя файла: ")
    old_str = ''
    new_str = '!'
    str_count = 0

    with open(file_name, 'r') as f:
        for line in f:
            strs = line.split()
            str_count += len(strs)
    print("Число вхождений строки: ", str_count)

    with open(file_name, 'wt') as f:
        for line in f:
            line.replace(old_str, new_str)


if __name__ == "__main__":
    main()
