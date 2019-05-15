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


def main():

    if len(sys.argv[:]) == 1:
        print(__doc__)
    try:
        ticket = input()
        if len(ticket) is 6:
            a = sum(map(int, ticket[:3]))
            b = sum(map(int, ticket[3:]))
            if a == b:
                print("Horrah! You've got a lucky number!")
            else:
                for i in range(int(ticket), 999999):
                    i = str(i)
                    a, b = sum(map(int, i[:3])), sum(map(int, i[3:]))
                    if a == b:
                        print("Next Lucky Ticket: " + i)
                        break
        else:
            print("A lucky number can be of 6 digits only")
    except:
        print("Please, enter numbers only")


if __name__ == "__main__":
    main()