# 5.18 Список простых чисел
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
    print('Простые числа: ', end= '')
    for number in range(1,101):
        if is_prime(number):
            print(f'{number}', end = ' ')

if __name__ == '__main__':
    main()
