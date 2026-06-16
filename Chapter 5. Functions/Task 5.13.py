# 5.13 Высота падения
G = 9.8

def falling_distance(t):
    d = (1 / 2) * G * t ** 2
    return d

def main():
    for i in range(1, 11):
        print(f'Высота падения при i = {i} - {falling_distance(i):,.2f} метров')

if __name__ == '__main__':
    main()
