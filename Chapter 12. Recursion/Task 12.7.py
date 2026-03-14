# 12.7 Рекурсивный метод возведения в степень

def main():
    value = int(input("Введите число: "))
    deg = int(input('В какую степень его возводить: '))
    print(degree(value = value, deg = deg))

def degree(value: int, deg: int) -> int:
    if deg == 1:
        return value
    elif deg == 0:
        return 1
    else:
        return value * (degree(value, deg - 1))

if __name__ == "__main__":
    main()
