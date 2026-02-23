# 7.12 Генерация простого числа
import math

def main():
    val = enter_number()
    lst = create_list(val)
    go_list(lst)

def enter_number():
    check = False
    while not check:
        try:
            number = int(input("Введите целое число больше 1: "))
            while number == 1 or number <= 0:
                number = int(input("Введите целое число больше 1: "))
        except ValueError:
            print("Ошибка значения.")
        else:
            check = True
            return number
    return None

def create_list(value):
    arr = []
    for i in range(2, value + 1):
        arr.append(i)
    return arr

def go_list(arr):
    print(*arr)
    for i in arr:
        print(f"Число {i} является {check_prime_number(i)}")

def check_prime_number(i):
    for x in range(2,int(math.sqrt(i)+1)):
        if i % x == 0:
            return "составное"
    return "простое"

if __name__ == "__main__":
    main()
