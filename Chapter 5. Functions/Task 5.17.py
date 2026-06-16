# 5.17 Простые числа
import math

def is_prime(value):
    if value == 1:
        return True
    elif value >= 2:
        for i in range(2, int(math.sqrt(value)) + 1):
            if value % i == 0:
                return False
        return True
    else:
        return None

def main():
    number = int(input('Введите число: '))
    if is_prime(number):
        print(f'Число {number} является простым')
    else:
        print(f'Число {number} не простое')

if __name__ == '__main__':
    main()
