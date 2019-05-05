import sys


class Envelope1:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    # def __lt__(self, other_envelope):
    #     if (self.width < other_envelope.width) & (self.height < other_envelope.height):
    #         return True
    #     else:
    #         return False


class Envelope2:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    # def __lt__(self, other_envelope):
    #     if (self.width < other_envelope.width) & (self.height < other_envelope.height):
    #         return True
    #     else:
    #         return False


def main():
    try:
        width1 = float(input('Введите ширину первого конверта: '))
        height1 = float(input('Введите высоту первого конверта: '))
        width2 = float(input('Введите ширину второго конверта: '))
        height2 = float(input('Введите высоту второго конверта: '))
        # if len(sys.argv[1:]) == 0:
        #     print("""Задайте размеры двух конвертов со сторонами (a,b) и (c,d)
        #             чтобы определить, можно ли один конверт вложить в другой
        #             """)
    except IndexError:
        print("Неверные параметры. Задайте ширину и высоту конвертов")
    except ValueError:
        print("Параметры заданы неверно. Задайте численно ширину и высоту конвертов")
    else:
        env1, env2 = Envelope1(width1, height1), Envelope2(width2, height2)
        if (env1.width > env2.width) & (env1.height > env2.height):
            print('Второй конверт можно вложить в первый')
        else:
            print('Второй конверт вложить не удастся!')


if __name__ == "__main__":
    main()