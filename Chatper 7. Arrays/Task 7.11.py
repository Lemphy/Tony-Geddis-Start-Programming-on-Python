# 7.11 Магический квадрат Ло Шу
import random
RESULT = 15
FIRST_DIAGONAL = 0
SECOND_DIAGONAL = 1

def main():
    mode = 0
    while mode != 3:
        mode = int(input(f'Режим работы программы\n'
                         f'1 - Задание с учебника\n'
                         f'2 - Рандомное заполнение списка\n'
                         f'3 - Выход\n'
                         f'Ответ: '))
        if mode == 1:
            square = [[4,9,2],
                      [3,5,7],
                      [8,1,6]]
            run(square)
        elif mode == 2:
            square = create_random_list()
            run(square)
        else:
            print('Выход из программы')

def create_random_list():
    square = [[0] * 3,
              [0] * 3,
              [0] * 3]
    for row in range(3):
        for col in range(3):
            square[row][col] = random.randint(1, 9)
    return square

def run(arr):
    print('Квадрат для проверки')
    print(*arr, sep='\n')
    if check_shou_lu(arr):
        print('Список является магическим квадратом Ло Шу')
    else:
        print('Список НЕ является магическим квадратом Ло Шу')
    print()

def check_shou_lu(arr):
    # создаем список для хранения флагов проверки на соответствие вертикали значению RESULT
    check_horizontal = [False] * len(arr)

    # Создаем список для хранения флагов проверки на соответствие горизонтали значению RESULT
    check_vertical = [False] * len(arr)

    # Создаем список для хранения флагов проверки на соответствие вертикалей значению RESULT
    check_diagonal = [False] * 2 # 2 - потому что вертикали две

    diagonal1 = 0 # накопитель для диагонали 1
    diagonal2 = 0 # накопитель для диагонали 2
    for row in range(len(arr)): # проходим по row элементам списка arr
        total_h = 0 # накопитель для текущей горизонтали
        total_v = 0 # накопитель для текущей вертикали
        diagonal1 += arr[row][row] # узнаем первую диагональ, начало с левого верхнего края
        diagonal2 +=  arr[row][len(arr[row]) - 1 - row] # узнаем вторую диагональ, начало с правого верхнего края
        for col in range(len(arr[row])): # проходим по col элементами вложенного списка arr
            total_h += arr[row][col] # узнаем горизонтали поочередно с 1 по 3
            total_v += arr[col][row] # узнаем вертикали поочередно с 1 по 3
        if total_h == RESULT: # если текущая горизонталь равняется RESULT, записываем True
            check_horizontal[row] = True
        if total_v == RESULT: # если текущая вертикаль равняется RESULT, записываем True
            check_vertical[row] = True
    if diagonal1 == RESULT: # если накопитель диагонали1 равняется RESULT, записываем True
        check_diagonal[FIRST_DIAGONAL] = True
    if diagonal2 == RESULT: # если накопитель диагонали2 равняется RESULT, записываем True
        check_diagonal[SECOND_DIAGONAL] = True

    # Проверяем содержимое всех списков с флагами
    result_h_v = False # переменная для получения точно ответа на соответствия ВСЕХ горизонталей и вертикалей
    if False not in check_horizontal and False not in check_vertical: # если флаг False не найден ни в одном из списков вертикалей и горизонталей
        result_h_v = True

    result_diagonal = False # переменная для получения точно ответа на соответствия ВСЕХ диагоналей
    if False not in check_diagonal: # если флаг False не найден в списке диагоналей
        result_diagonal = True

    if result_h_v and result_diagonal: # если ОБА результата истинны, то возвращаем истину
        return True
    else: # иначе возвращаем ложь
        return False

if __name__ == '__main__':
    main()
