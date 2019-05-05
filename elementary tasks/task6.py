import sys


def main():
    try:
        ticket = input()
        if len(ticket) is 6:
            a = sum(map(int, ticket[:3]))
            b = sum(map(int, ticket[3:]))
            if a == b:
                print("Ура! У вас счастливый билет!")
            else:
                for i in range(int(ticket), 999999):
                    i = str(i)
                    a, b = sum(map(int, i[:3])), sum(map(int, i[3:]))
                    if a == b:
                        print("Next Lucky Ticket: " + i)
                        break
        else:
            print("Счастливый билет может быть только из 6 цифр")
    except:
        print("Пожалуйста, вводите только цифры")


if __name__ == "__main__":
    main()