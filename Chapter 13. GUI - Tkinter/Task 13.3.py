import tkinter as tk

class MyGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Task 13.3')
        self.geometry('250x150+400+400')
        self.frame1 = tk.Frame()
        self.frame2 = tk.Frame()
        self.frame3 = tk.Frame()
        self.frame4 = tk.Frame()
        self.label1 = tk.Label(self.frame1, text = 'Объем бензина в галлонах:')
        self.entry1 = tk.Entry(self.frame1, width = 10)
        self.label2 = tk.Label(self.frame2, text = 'Число миль:')
        self.entry2 = tk.Entry(self.frame2, width = 10)
        self.label3 = tk.Label(self.frame3, text = 'Показатель миль на галон: ', pady = 20)
        self.var = tk.StringVar()
        self.label4 = tk.Label(self.frame3, textvariable= self.var)
        self.result_button = tk.Button(self.frame4, text = 'Рассчитать', command = self.calc)
        self.label1.pack(side = 'left')
        self.entry1.pack(side = 'left')
        self.label2.pack(side = 'left')
        self.entry2.pack(side = 'left')
        self.label3.pack(side = 'left')
        self.label4.pack(side = 'left')
        self.result_button.pack()
        self.frame1.pack(anchor= 'nw')
        self.frame2.pack(anchor= 'nw')
        self.frame3.pack(anchor= 'center')
        self.frame4.pack()

    def calc(self):
        var1 = int(self.entry1.get()) # галлоны
        var2 = int(self.entry2.get()) # мили
        value = var2 / var1
        self.var.set(str(value))

if __name__ == '__main__':
    my_gui = MyGui()
    my_gui.mainloop()
