"""
Elementary Task #3

Сортировка треугольников
----------------

Программа выполняет вывод треугольников в порядке убывания
их площади.
• Расчёт площади треугольника производится по формуле Герона.
• Каждый треугольник определяется именем и длинами его сторон.
Формат ввода (разделитель - запятая):
    <имя>, <длина стороны>, <длина стороны>, <длина стороны>
• Приложение должно обрабатывать ввод чисел с плавающей точкой.
• Ввод должен быть нечувствителен к регистру, пробелам, табам.
•	Вывод данных должен быть следующем примере:
============= Triangles list: ===============
1. [Triangle first]: 17.23 сm
2. [Triangle 22]: 13 cm
3. [Triangle 1]: 1.5 cm

После добавления каждого нового треугольника программа спрашивает, хочет ли
пользователь добавить ещё один. Если пользователь ответит “y” или “yes” (без учёта регистра),
программа попросит ввести данные для ещё одного треугольника, в противном случае – выводит
результат в консоль.

"""
# удаление пробелов про вводе с пом. str.replace
import sys


class Triangle:
    def __init__(self, name, side_a, side_b, side_c):
        """
        The constructor for Triangle class.

        Parameters:
            name (str): The triangle name.
            side_a, side_b, side_c (float): The triangle sides.
        """
        self.name = name.strip('\t').strip(' ').lower().title()
        self.sides = [float(s.strip('\t').strip(' ')) for s in [side_a, side_b, side_c]]
        if not (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            print("Such a trianle can't exist")

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
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __str__(self):
        return '{name}: {area:g} cm'.format(name=self.name, area=self.area)

    def __repr__(self):
        return self.area


def main():

    if len(sys.argv) == 1:
        print(__doc__)

    triange_list = []

    while True:
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
            if repeat not in ('y' or 'yes'):
                break

    print('Triangles list'.center(43, '='))
    triange_list.sort()
    for triangle in triange_list:
        print(triangle)


if __name__ == "__main__":
    main()
