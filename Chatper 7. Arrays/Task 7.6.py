# 7.6 Больше числа n

def main():
    mylist = list(range(10,60))
    n = int(input('Введите число: '))
    high_n = check_n(mylist, n)
    print('Список:', *mylist)
    print(f'Числа больше {n}:', *high_n)

def check_n(lst, n):
    return [i for i in lst if i > n]

if __name__ == '__main__':
    main()
