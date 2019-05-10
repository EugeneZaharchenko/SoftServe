class Triangle:
    def __init__(self, name, side_a, side_b, side_c):
        """
        The constructor for Triangle class.

        Parameters:
            name (str): The triangle name.
            side_a, side_b, side_c (float): The triangle sides.
        """
        self.name = name.strip('\t').strip(' ').lower().title()
        self.side_a = float(side_a.strip('\t').strip(' '))
        self.side_b = float(side_b.strip('\t').strip(' '))
        self.side_c = float(side_c.strip('\t').strip(' '))
        self.sides = [self.side_a, self.side_b, self.side_c]
        self._area = 0

    @property
    def area(self):
        """
        Calculates the square of given triangle using Heron formula:
        Area = √s(s - a)(s - b)(s - c)

        Parameters:
            self: The Triangle class instance.

        Returns:
            _area (float): The area of the given triangle.
        """
        p = sum(self.sides) / 2
        mult_val = 1
        for s in self.sides:
            mult_val *= (p-s)
        p *= mult_val
        self._area = p ** 0.5
        return self._area

    def __lt__(self, other):
        self.area < other._area

    def __gt__(self, other):
        self.area > other._area

    def __str__(self):
        return '{name}: {area:g} cm'.format(name=self.name, area=self.area)

    def __repr__(self):
        return self._area


def main():
    """
    Программа выводит треугольники в порядке убывания их площади.
    Введите данные о треугольнике: имя, длина каждой из сторон.
    """
    # instructions =

    # После подсчета, если хотите продолжить работу программы сначала - введите y или yes

    triange_list = []
    repeat = True

    while repeat:
        try:
            data = input('Введите имя, сторону1, сторону2, сторону3: ').strip().split(',')
            if not data[0].isalpha:
                raise ValueError('Задайте верно имя треугольника')
            elif len(data[1:]) != 3:
                raise ValueError
            elif not all([s for s in data[1:] if s.isnumeric()]):
                raise ValueError
        except ValueError:
            print("Параметры заданы неверно. Задайте имя треугольника и параметры трех его сторон")
            continue
        else:
            triange_list.append(Triangle(*data))
        finally:
            repeat = input('Хотите продолжить? (y/n): ')
            repeat.lower().strip()
            if ('y' or 'yes') not in repeat:

                repeat = False

    print('Triangles list'.center(43, '='))
    for triangle in sorted(triange_list):
        print(triangle)


if __name__ == "__main__":
    main()
