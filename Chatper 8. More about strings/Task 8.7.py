# 8.7 Анализ символов
def main():
    infile = open('text.txt','r')
    text = infile.readlines()
    infile.close()
    for i in range(len(text)):
        text[i] = text[i].rstrip()
    isdigit = 0 # цифры
    isupper = 0 # большие буквы
    islower = 0 # маленькие буквы
    isspace = 0 # пробельные символы
    for i in text:
        for j in i:
            if j.isdigit():
                isdigit += 1
            elif j.isupper():
                isupper += 1
            elif j.islower():
                islower += 1
            elif j.isspace():
                isspace += 1
    print(f"Количество букв в файле в верхнем регистре: {isupper}\n"
          f"Количество букв в файле в нижнем регистре: {islower}\n"
          f"Количество цифр в файле: {isdigit}\n"
          f"Количество пробельных символов в файле: {isspace}")

if __name__ == "__main__":
    main()
