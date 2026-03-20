import tkinter as tk

class MyGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x150+400+400')
        self.first_frame = tk.Frame(self)
        self.second_frame = tk.Frame(self)
        self.var = tk.StringVar()
        self.var_label = tk.Label(self.first_frame, textvariable= self.var, pady = 20)
        self.one_button = tk.Button(self.second_frame, text = 'sinister', command= lambda: self.show_russian('sinister'))
        self.two_button = tk.Button(self.second_frame, text = 'dexter', command= lambda: self.show_russian('dexter'))
        self.three_button = tk.Button(self.second_frame, text = 'medium', command= lambda: self.show_russian('medium'))
        self.var_label.pack()
        self.one_button.pack(side = 'left')
        self.two_button.pack(side = 'left')
        self.three_button.pack(side = 'left')
        self.first_frame.pack()
        self.second_frame.pack()


    def show_russian(self, name):
        if name == 'sinister':
            self.var.set('Левый')
        elif name == 'dexter':
            self.var.set('Правый')
        elif name == 'medium':
            self.var.set('Центральный')

if __name__ == '__main__':
    my_gui = MyGui()
    my_gui.mainloop()
