# 13.7 Междугородные звонки

import tkinter as tk

class MyGui(tk.Tk):
    def __init__(self):
        super().__init__()
        # создаем макет окна
        self.title('Task 13.7')
        self.category = tk.Frame(self)
        self.input_time = tk.Frame(self)
        self.show_price = tk.Frame(self)
        self.buttons = tk.Frame(self)

        self.v_rb = tk.IntVar()
        self.rb1 = tk.Radiobutton(self.category, text = 'Дневное время (с 6:00 до 17:59). Тариф в минуту: 10 руб.', value = 1, variable= self.v_rb)
        self.rb2 = tk.Radiobutton(self.category, text = 'Вечернее время (с 18:00 до 23:59). Тариф в минуту: 12 руб.', value = 2, variable= self.v_rb)
        self.rb3 = tk.Radiobutton(self.category, text = 'Непиковый период (с полуночи до 5:59). Тариф в минуту: 5 руб.', value = 3, variable= self.v_rb)

        self.rb1.pack(side = 'left')
        self.rb2.pack(side = 'left')
        self.rb3.pack(side = 'left')

        self.label1 = tk.Label(self.input_time, text = 'Продолжительность звонка в минутах:')
        self.label2 = tk.Entry(self.input_time, width= 10)

        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')

        self.val = tk.StringVar()
        self.label3 = tk.Label(self.show_price, text = ' Стоимость звонка:')
        self.label4 = tk.Label(self.show_price, textvariable= self.val)

        self.label3.pack(side = 'left')
        self.label4.pack(side = 'left')

        self.button1 = tk.Button(self.buttons, text = 'Рассчитать стоимость', command = self.calc)
        self.button2 = tk.Button(self.buttons, text = ' Закрыть', command = self.destroy)

        self.button1.pack(side = 'left')
        self.button2.pack(side = 'left')

        self.category.pack()
        self.input_time.pack()
        self.show_price.pack()
        self.buttons.pack()

    def calc(self):
        temp = int(self.label2.get())
        if self.v_rb.get() == 1:
            self.val.set(f"{temp*10}")
        elif self.v_rb.get() == 2:
            self.val.set(f"{temp*12}")
        elif self.v_rb.get() == 3:
            self.val.set(f"{temp*5}")

if __name__ == '__main__':
    my_gui = MyGui()
    my_gui.mainloop()
