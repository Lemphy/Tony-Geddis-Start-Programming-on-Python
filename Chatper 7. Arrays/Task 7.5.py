# 7.5 Проверка допустимости номера расходного счета

def main():
    infile = open('charge_accounts.txt', 'r', encoding= 'UTF-8')
    temp = infile.readlines()
    infile.close()
    for i in range(len(temp)):
        temp[i] = int(temp[i].rstrip())
    user_answer = int(input('Номер расходного счета: '))
    if user_answer in temp:
        print('Номер допустимый')
    else:
        print('Номер недопустимый')

if __name__ == '__main__':
    main()
