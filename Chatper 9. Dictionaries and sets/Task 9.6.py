# 9.6 Анализ файла
def main():
    lst = open_files() # получаем из функции кортеж состоящих из двух множеств
    if lst is not None: # если кортеж не None
        val1, val2 = lst
        show_union(val1,val2)
        show_all_words(val1,val2)
        show_difference(val1,val2)
        show_symmetric_difference(val1,val2)

def show_union(val1, val2):
    val3 = val1 | val2
    print(f"\nСписок всех уникальных слов, содержащихся в обоих файлах.")
    print_result(val3)

def show_all_words(val1,val2):
    val3 = val1 & val2 # конкатенируем оба списков
    print("\nСписок слов, входящих в оба файла одновременно.")
    print_result(val3)

def show_difference(val1,val2):
    val3 = val1 - val2
    print("\nСписок слов из первого файла, не входящих во второй")
    print_result(val3)
    val3 = val2 - val1
    print("\nСписок слов из второго файла, не входящих в первый")
    print_result(val3)

def show_symmetric_difference(val1,val2):
    val3 = val1 ^ val2
    print("\nСписок слов, не входящих в оба файла одновременно")
    print_result(val3)

def open_files():
    filename1 = input("Введите название файла 1\n>>> ")
    filename2 = input("Введите название файла 2\n>>> ")
    try:
        if filename1.endswith('.txt') and filename2.endswith('.txt'):
            infile1 = open(filename1, 'r', encoding='UTF-8')
            infile2 = open(filename2, 'r', encoding='UTF-8')
            res1 = infile1.read().lower().split() # получаем из файла список слов в малом регистре разделенный пробелами
            res2 = infile2.read().lower().split()
            infile1.close()
            infile2.close()
            for i in range(len(res1)): # проходим оба списка для удаления из слов ненужных символов
                res1[i] = res1[i].strip(',.!?"()')
            for i in range(len(res2)):
                res2[i] = res2[i].strip(',.!?"()')
            res1 = set(res1) # преобразуем список в множество
            res2 = set(res2)
            return res1, res2 # возвращаем результат работы функции в виде двух множеств
        else:
            print(f"Один из файлов(либо оба) не соответствуют требуемому расширению.")
    except FileNotFoundError:
        print(f"Один из файлов(либо оба) не обнаружен(ы).")
    return None

def print_result(arg): # проверка на конец списка и печать точки в конце
    temp = 0
    if arg: # если в множестве есть хоть что-то значит True
        for i in arg:
            if temp != len(arg) - 1: # если накапливающая переменная не равна последнему элементу списка
                print(i, end=", ")
                temp += 1
            else:
                print(i, end=".")
    else: # если множество пустое - False
        print('Список пуст.')

if __name__ == "__main__":
    main()
