# 5.7 Сидячие места на стадионе

CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

def calc_price_of_tickets(a,b,c):
    a *= CLASS_A
    b *= CLASS_B
    c *= CLASS_C
    return a,b,c

def main():
    sold_class_A = int(input('Введите количество проданных билетов класса А: '))
    sold_class_B = int(input('Введите количество проданных билетов класса B: '))
    sold_class_C = int(input('Введите количество проданных билетов класса С: '))
    a_price, b_price, c_price = calc_price_of_tickets(sold_class_A, sold_class_B, sold_class_C)
    print(f"Доход с билетов\n"
          f"А класса: {a_price:,.2f}$\n"
          f"B класса: {b_price:,.2f}$\n"
          f"C класса: {c_price:,.2f}$\n"
          f"Общий доход: {a_price + b_price + c_price:,.2f}$")

if __name__ == '__main__':
    main()
