# import sys


class Envelope1:
    def __init__(self, width, height):
        self.width = float(width.strip())
        self.height = float(height.strip())

    # def __lt__(self, other_envelope):
    #     if (self.width < other_envelope.width) & (self.height < other_envelope.height):
    #         return True
    #     else:
    #         return False


class Envelope2:
    def __init__(self, width, height):
        self.width = float(width.strip())
        self.height = float(height.strip())

    # def __lt__(self, other_envelope):
    #     if (self.width < other_envelope.width) & (self.height < other_envelope.height):
    #         return True
    #     else:
    #         return False

# class Workflow:


def main():

    instructions = """
        Введите размеры конвертов по одному за раз.
        После подсчета, если хотите продолжить работу программы сначала - введите y или yes
        """

    repeat = True

    while repeat:
        try:
            width1 = input('Введите ширину первого конверта: ')
            height1 = input('Введите высоту первого конверта: ')
            width2 = input('Введите ширину второго конверта: ')
            height2 = input('Введите высоту второго конверта: ')

            # create two instances of Envelope class with given arguments
            env1, env2 = Envelope1(width1, height1), Envelope2(width2, height2)

        except IndexError:
            print("Неверные параметры. Задайте ширину и высоту конвертов")
            continue
        except ValueError:
            print("Параметры заданы неверно. Задайте численно ширину и высоту конвертов")
            continue
        else:
            if ((env1.width > env2.width) & (env1.height > env2.height)
                & (env1.height > env2.width) & (env1.width > env2.height)):
                print('Второй конверт можно вложить в первый')
            else:
                print('Второй конверт вложить не удастся!')
        finally:
            again = input('Хотите продолжить? (y/n): ')
            again.lower().strip()
            if ('y' or 'yes') not in again:
                repeat = False

    # if len(sys.argv[:]) == 1:
    #     print(instructions)


if __name__ == "__main__":
    main()
