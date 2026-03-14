# 12.2 Рекурсивное умножение

def main():
    print(recursive_multiplication(x = 7, y = 4))

def recursive_multiplication(x, y):
    if x == 0: # базовый случай
        return 0
    else: # рекурсивный случай
        return y + recursive_multiplication(x-1,y)

if __name__ == "__main__":
    main()
