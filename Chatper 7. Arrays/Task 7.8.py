# 7.8 Поиск имени
LIST = 200

def main():
    boys, girls = read_files()
    find = input_name()
    for i in find:
        if i in boys and i in girls:
            print(f"{i} находится в обоих списках.")
        elif i in boys:
            print(f"{i} находится среди самых популярных мужских имен.")
        elif i in girls:
            print(f"{i} находится среди самых популярных женских имен.")
        else:
            print(f'{i} не найдено.')

def read_files():
    infile_boys = open('BoyNames.txt', 'r')
    infile_girls = open('GirlNames.txt', 'r')
    boys = infile_boys.readlines()
    girls = infile_girls.readlines()
    infile_boys.close()
    infile_girls.close()
    for i in range(LIST):
        girls[i] = girls[i].rstrip()
    for x in range(LIST):
        boys[x] = boys[x].rstrip()
    return boys, girls

def input_name():
    check = False
    while not check:
        try:
            mode = 0
            while mode !=1 and mode !=2 and mode!= 3:
                mode = int(input("Выбирите режим работы.\n"
                                 "1 - ввести имя девочки\n"
                                 "2 - ввести имя мальчика\n"
                                 "3 - ввести имя девочки И мальчика\n"
                                 "Ответ: "))
            if mode == 1:
                name = []
                name.append(input("Введите имя девочки для поиска: "))
            elif mode == 2:
                name = []
                name.append(input("Введите имя мальчика для поиска: "))
            elif mode == 3:
                names = []
                names.append(input("Введите имя девочки для поиска: "))
                names.append(input("Введите имя мальчика для поиска: "))
        except:
            print("Произошла ошибка")
        else:
            check = True
            if mode == 1 or mode == 2:
                return name
            else:
                return names

if __name__ == "__main__":
    main()
