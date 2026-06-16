# 5.14 Кинетическая энергия

def kinetic_energy(weight, speed):
    return (1 / 2) * weight * speed ** 2

def main():
    weight = int(input('Введите массу тела в кг: '))
    speed = int(input('Введите скорость тела в м/c: '))
    print(f'Кинетическая энергия тела: {kinetic_energy(weight, speed)}')

if __name__ == '__main__':
    main()
