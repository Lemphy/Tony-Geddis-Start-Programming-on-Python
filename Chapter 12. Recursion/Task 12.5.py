# 12.5 Рекурсивная сумма списка

def main():
    mylist = list(range(5))
    print(total_list(mylist))

def total_list(arg):
    n = len(arg) # узнаем длину списка
    if n == 1: # базовый случай
        return arg[n - 1]
    else: # рекурсивный случай
        return arg[n - 1] + (total_list(arg[0 : n - 1])) # уменьшаем список до 1 элемента, узнаем значение этого элемента, прибавляем это значение

if __name__ == "__main__":
    main()
