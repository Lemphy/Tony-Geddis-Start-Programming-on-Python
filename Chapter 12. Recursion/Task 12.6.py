# 12.6 Сумма чисел

def main():
    value = int(input('Введите число: '))
    print('Число:',count_values(value))

def count_values(value):
    if value == 1: # базовый случай
        return 1
    else: # рекурсивный случай
        return value + count_values(value - 1)

if __name__ == "__main__":
    main()
