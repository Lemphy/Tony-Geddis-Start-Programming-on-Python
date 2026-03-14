# 12.8 Функция Аккермана

def main():
    print(ackermann(2,3))

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

if __name__ == "__main__":
    main()
