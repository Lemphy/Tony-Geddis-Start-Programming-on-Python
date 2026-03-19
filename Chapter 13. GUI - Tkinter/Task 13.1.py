# 13.1 ФИО и адрес

import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('200x120')
        self.main_window.title('ФИО и адрес')
        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.var = tkinter.StringVar()
        self.first_label = tkinter.Label(self.first_frame, textvariable= self.var)
        self.show_button = tkinter.Button(self.second_frame, text = 'Показать инфо', command = self.show_text)
        self.exit_button = tkinter.Button(self.second_frame, text = 'Выход', command = self.main_window.destroy)
        self.first_frame.pack()
        self.first_label.pack()
        self.second_frame.pack()
        self.show_button.pack(side = 'left')
        self.exit_button.pack(side = 'left')
        tkinter.mainloop()

    def show_text(self):
        self.var.set('\n162390. Россия. Вологодская обл,.\n'
                     'г. Великий Устюг,\n'
                     'Почта Деда Мороза\n')

if __name__ == '__main__':
    my_gui = MyGui()
