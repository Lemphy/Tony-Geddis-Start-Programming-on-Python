# 8.5 Алфавитный переводчик номера телефона
def main():
    lst_1 = [2,3,4,5,6,7,8,9]
    lst_2 = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    response = input('Введите 10-символьный номер телефона в формате XXX-XXX-XXXX: ')
    response_lst = response.split('-')
    print(f"Вы ввели: {response_lst}")
    temp = ""
    counter = 0
    for i in range(len(response_lst)): # проходим введенный пользователем список
        for j in response_lst[i].upper(): # заходим в строковое значение елемента списка, j проверяет каждую букву i элемента
            if j.isalpha(): # если мы видим что значение это буква
                for x in range(len(lst_2)): # проходим готовый список буквенных символов
                    check = lst_2[x].find(j) # если находим символ в x элементе
                    if check != -1: # если метод find() нашел значение индекса элемента j
                        temp += f"{lst_1[x]}"  # присваиваем значение цифры относящееся к этой букве
            else:
                temp += f"{j}"
        if counter < 2: # печатаем разделители когда заканчиваем проверять i значение списка
            counter += 1
            temp += f"-"
    print(temp)

if __name__ == "__main__":
    main()
