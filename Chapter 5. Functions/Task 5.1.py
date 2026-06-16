# 5.1 Конвертер километров
MIL = 0.6214

def calc_mil(arg1):
    return arg1 * MIL

def main():
    distance = int(input('Введите расстояние в километрах: '))
    print(f'Расстояние в милях: {calc_mil(distance):,.2f}')

if __name__ == '__main__':
    main()
