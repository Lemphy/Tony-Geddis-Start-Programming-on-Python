# 13.5 Налог на недвижимость

import tkinter as tk

class MyGui(tk.Tk):
    def __init__(self):
        super().__init__()
        # создаем макет окна
        self.title('Task 13.5')
        self.geometry('250x100+100+100')
        self.first_frame = tk.Frame(self)
        self.second_frame = tk.Frame(self)
        self.third_frame = tk.Frame(self)
        self.fourth_frame = tk.Frame(self)
        # заполняем первую рамку
        self.label1 = tk.Label(self.first_frame, text = 'Стоимость имущества:')
        self.entry1 = tk.Entry(self.first_frame, width= 10)
        self.label1.pack(side = 'left')
        self.entry1.pack(side = 'left')
        self.first_frame.pack(anchor= 'nw')
        # заполняем вторую рамку
        self.price = tk.StringVar()
        self.label2_1 = tk.Label(self.second_frame, text = 'Оценочная стоимость:')
        self.label2_2 = tk.Label(self.second_frame, textvariable= self.price)
        self.label2_1.pack(side = 'left')
        self.label2_2.pack(side = 'left')
        self.second_frame.pack(anchor= 'nw')
        # заполняем третью рамку
        self.tax = tk.StringVar()
        self.label3_1 = tk.Label(self.third_frame, text = 'Налог:')
        self.label3_2 = tk.Label(self.third_frame, textvariable= self.tax)
        self.label3_1.pack(side = 'left')
        self.label3_2.pack(side = 'left')
        self.third_frame.pack(anchor= 'nw')
        # заполняем четвертую рамку
        self.Button1 = tk.Button(self.fourth_frame, text = 'Рассчитать', command = self.calc)
        self.Button2 = tk.Button(self.fourth_frame, text = 'Выход', command = self.destroy)
        self.Button1.pack(side = 'left')
        self.Button2.pack(side = 'left')
        self.fourth_frame.pack()

    def calc(self):
        value = int(self.entry1.get())
        price = value * 0.6
        self.price.set(f"{price} $")
        self.tax.set(f"{price/100*0.75} $")

if __name__ == '__main__':
    my_gui = MyGui()
    my_gui.mainloop()
