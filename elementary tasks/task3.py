import sys


def main():
    input_list = input('Введите имя, сторону1, сторону2, сторону3: ').strip(' \t').split(',')
    triange_name = input_list[0].strip(' \t').lower()
    a, b, c = [float(x.strip(' \t')) for x in input_list[1:]]
    p = (a + b + c) / 2
    heron_area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('Triangles list'.center(43, '='))
    print('Triangle ', triange_name, ': ', str(heron_area), ' cm')


if __name__ == "__main__":
    main()
