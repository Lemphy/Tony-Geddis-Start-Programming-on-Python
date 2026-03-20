# 13.6 Авторемонтная фирма "Автоцех"

import tkinter as tk
import tkinter.messagebox

class MyGui(tk.Tk):
    def __init__(self):
        super().__init__()
        # создаем макет окна
        self.title('Task 13.6')
        self.service = tk.Frame(self)
        self.prices = tk.Frame(self)
        # переменные для хранения чекбокса
        self.v_name1 = tk.IntVar()
        self.v_name2 = tk.IntVar()
        self.v_name3 = tk.IntVar()
        self.v_name4 = tk.IntVar()
        self.v_name5 = tk.IntVar()
        self.v_name6 = tk.IntVar()
        self.v_name7 = tk.IntVar()
        # создать чекбоксы
        self.name1 = tk.Checkbutton(self.service, text = 'Замена масла - 500.00 руб.', variable= self.v_name1)
        self.name2 = tk.Checkbutton(self.service, text = 'Смазочные работы - 300.00 руб.', variable= self.v_name2)
        self.name3 = tk.Checkbutton(self.service, text = 'Промывка радиатора - 700.00 руб.', variable= self.v_name3)
        self.name4 = tk.Checkbutton(self.service, text = 'Замена жидкости в трансмиссии - 1000.00 руб.', variable=self.v_name4)
        self.name5 = tk.Checkbutton(self.service, text = 'Осмотр - 800.00 руб.', variable=self.v_name5)
        self.name6 = tk.Checkbutton(self.service, text = 'Замена глушителя выхлопа - 1300.00 руб.', variable=self.v_name6)
        self.name7 = tk.Checkbutton(self.service, text = 'Перестановка шин - 1300.00 руб.', variable=self.v_name7)
        # упаковать чекбоксы
        self.name1.pack()
        self.name2.pack()
        self.name3.pack()
        self.name4.pack()
        self.name5.pack()
        self.name6.pack()
        self.name7.pack()
        # создать кнопки управления
        self.Button1 = tk.Button(self.prices, text = 'Рассчитать', command = self.calc_price)
        self.Button2 = tk.Button(self.prices, text = 'Выход', command = self.destroy)

        self.Button1.pack(side = 'left')
        self.Button2.pack(side = 'left')

        self.service.pack()
        self.prices.pack()

    def calc_price(self):
        total = 0
        if self.v_name1.get():
            total += 500
        if self.v_name2.get():
            total += 300
        if self.v_name3.get():
            total += 700
        if self.v_name4.get():
            total += 1000
        if self.v_name5.get():
            total += 800
        if self.v_name6.get():
            total += 1300
        if self.v_name7.get():
            total += 1300
        tkinter.messagebox.showinfo(title = 'Результат', message = f"Общая стоимость услуг: {total} руб.")

if __name__ == '__main__':
    my_gui = MyGui()
    my_gui.mainloop()
