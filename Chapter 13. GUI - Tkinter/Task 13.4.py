# 13.4 Из шкалы Цельсия в шкалу Фаренгейта

import tkinter as tk

class MyGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Task 13.4')
        self.geometry('250x100+400+400')
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.label1 = tk.Label(self.frame1, text = 'Температура по шкале Цельсия:')
        self.entry1 = tk.Entry(self.frame1, width= 10)
        self.label1.pack(side = 'left')
        self.entry1.pack(side = 'left')
        self.frame1.pack(anchor= 'nw')
        self.label2 = tk.Label(self.frame2, text = 'Температура по шкале Фаренгейта:')
        self.var = tk.StringVar()
        self.label3 = tk.Label(self.frame2, textvariable=self.var)
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')
        self.frame2.pack(anchor= 'nw')
        self.button = tk.Button(self.frame3, text = 'Рассчитать', command = self.calc)
        self.button.pack()
        self.frame3.pack()

    def calc(self):
        Celsium = int(self.entry1.get())
        Farengeit = (9/5*Celsium)+32
        self.var.set(str(Farengeit))

if __name__ == '__main__':
    my_gui = MyGui()
    my_gui.mainloop()
