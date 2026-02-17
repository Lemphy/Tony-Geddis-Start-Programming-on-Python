import random
TOTAL = 15

def main():
    cube = [[4,9,2],
            [3,5,7],
            [8,1,6]]
   # заполнение матрицы случайными числами
   # for i in range(MAX):
   #     for x in range(MAX):
   #         cube[i][x] = random.randint(1,9)
    print(*cube, sep = "\n")
    check_shou_lu(cube)

def check_shou_lu(arr):
    check_h = False
    check_v = False
    check_d1 = False
    check_d2 = False
    diagonal_a = 0
    diagonal_b = 0
    for row in range(len(arr)):
        total_h = 0
        total_v = 0
        diagonal_a += arr[row][row] # первая диагональ
        diagonal_b += arr[row][len(arr) - 1 - row] # вторая диагональ
        for col in range(len(arr)):
            total_h += arr[row][col]  # вертикали
            total_v += arr[col][row]  # горизонтали
        if total_h == TOTAL:
            check_h = True
        else:
            check_h = False
        if total_v == TOTAL:
            check_v = True
        else:
            check_v = False

    if diagonal_a == TOTAL:
        check_d1 = True
    else:
        check_d1 = False
    if diagonal_b == TOTAL:
        check_d2 = True
    else:
        check_d2 = False
    if not check_h and not check_d1 and not check_d2 and not check_v:
        return print("Не является магическим квадратом.")
    else:
        return print("Это магический квадрат")

if __name__ == "__main__":
    main()
