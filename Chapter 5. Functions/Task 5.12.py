#5.12 Максимальное из двух значений

def check_max_value(arg1, arg2):
    if arg1 > arg2:
        return arg1
    elif arg2 > arg1:
        return arg2
    else:
        return 'одинаковы'

def main():
    val1 = int(input('Введите число 1: '))
    val2 = int(input('Введите число 2: '))
    print(f'Максимальное из двух значений: {check_max_value(val1, val2)}')

if __name__ == '__main__':
    main()
