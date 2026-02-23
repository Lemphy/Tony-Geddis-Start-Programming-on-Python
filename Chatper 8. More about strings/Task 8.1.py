# 8.1 Инициалы
def main():
    name = input("Введите ФИО:")
    print(create_initials(name))

def create_initials(name):
    temp = name.split()
    initials = ''
    for i in temp:
        initials += f"{i[0].upper()}."
    return initials

if __name__ == "__main__":
    main()
