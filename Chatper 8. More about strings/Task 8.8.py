# 8.8 Корректор предложений
def main():
    sentence = input("> ")
    correct = correct_sentence(arg = sentence)
    print(correct)

def correct_sentence(arg):
    arr = arg.split()
    print(arr)
    next_word = True
    sentence = ''
    end_of_sentence = ('.', '?', '!')
    for i in range(len(arr)): # проход по индексам(i) списка arr
        end_ch = arr[i][-1:] # узнаем последний символ i элемента списка
        if next_word: # если было замечено начало либо последним символом предыдущего слова был знак окончания предложения.
            sentence += f"{arr[i][:1].upper() + arr[i][1:]}" # Добавляем копию первой буквы i элемента и добавляем копию остальных букв состоящих в i элементе.
            if i == (len(arr)-1) and end_ch not in end_of_sentence: # если слово только одно и пользователь забыл добавить знак конца предложения
                sentence += f"{end_of_sentence[0]}" # добавляем точку в конец
            else:
                sentence += f" " # если слово не одно, то добавляем пробел в конец
        else:
            sentence += f"{arr[i][:]} " # если последним символом был НЕ знак окончания предложения, то добавляем копию i элемента без изменений

        if end_ch not in end_of_sentence: # если конечного символа НЕТУ в кортеже end_of_sentence, то меняем на False чтобы не выполнился первый if итерации.
            next_word = False
        else:
            next_word = True # если находим конечный символ, то выполняется первый if в итерации и добавляется начало предложения с большой буквы.
    return sentence

if __name__ == "__main__":
    main()
