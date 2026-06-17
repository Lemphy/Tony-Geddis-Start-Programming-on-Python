# 6.11 Генератор персональной веб-страницы

def generate_file(name, desc):
    filename = 'description.html'
    outfile = open(filename, 'w', encoding= 'UTF-8')
    outfile.write(f'<html>\n'
                  f'<head>\n'
                  f'</head>\n'
                  f'<body>\n'
                  f'  <center>\n'
                  f'    <h1>{name}</h1>\n'
                  f'  </center>\n'
                  f'  <hr />\n'
                  f'  {desc}\n'
                  f'  <hr />\n'
                  f'</body\n'
                  f'</html>\n')
    outfile.close()
    print(f'Файл {filename} успешно записан.')

def enter_data():
    name = input('Введите свое имя: ')
    description = input('Опишите себя: ')
    return name, description

def main():
    name, desc = enter_data()
    generate_file(name, desc)

if __name__ == '__main__':
    main()
