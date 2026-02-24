# 8.12 Молодежный жаргон
def main():
    user_input = input("Предложение\n>>> ")
    print(f"Молодежный жаргон: {convert_young(user_input)}")

def convert_young(arg):
    temp = arg.split() # создаем список из введенной строки
    sentence = '' # накопительная переменная для новой строки
    end = 'ки' # окончание каждого слова
    space = ' ' # пробелы
    for i in range(len(temp)): # проходим каждый элемент списка
        sentence += f"{temp[i][1:] + temp[i][:1] + end + space}" # добавляем в накопительную переменную срезы из списка, окончание каждого слова и пробел
    return sentence.upper()

if __name__ == "__main__":
    main()
