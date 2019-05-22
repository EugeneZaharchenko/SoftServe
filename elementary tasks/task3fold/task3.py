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
        self.name, self.side_a, self.side_b, self.side_c = self.valid(name, side_a, side_b, side_c)
        self.sides = [float(s) for s in [side_a, side_b, side_c]]
        self._area = 0

    @staticmethod
    def valid(name, side_a, side_b, side_c):
        _name = name.strip('\t').strip(' ').lower().title()
        if not (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            _side_a = side_a
            _side_b = side_b
            _side_c = side_c
        else:
            raise IndexError
        return _name, _side_a, _side_b, _side_c

    @property
    def area(self):
        """
        Calculates the square of given triangle using Heron formula:
        Area = √s(s - a)(s - b)(s - c)
        :return (float): triangle's area
        """
        p = sum(self.sides) / 2
        mult_val = 1
        for s in self.sides:
            mult_val *= (p-s)
        p *= mult_val
        self._area = p ** 0.5
        return self._area

    # reload class magic methods
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
            # receive user's data
            data = input('Please enter name, side1, side2, side3: ').strip().split(',')
            if not data[0].isalpha:
                raise ValueError('Enter a correct triangle name.')
            elif len(data[1:]) != 3:
                raise ValueError
            elif not all([s for s in data[1:] if s.isnumeric()]):
                raise ValueError
        except ValueError:
            print("Wrong parameters. Please enter triangle's name and values of its sides.")
            continue
        else:
            try:
                triange_list.append(Triangle(*data))
            except IndexError:
                print("Such a triangle can't exist")
        finally:
            repeat = input('Do you want to continue? (y/n): ')
            repeat.lower().strip()
            if repeat not in ('y' or 'yes'):
                break

    print('Triangles list'.center(43, '='))
    triange_list.sort()
    for triangle in triange_list:
        print(triangle)


if __name__ == "__main__":
    main()
