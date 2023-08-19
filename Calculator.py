import tkinter


class Calc:
    def __init__(self):
        self.okno = tkinter.Tk()
        self.okno.title("Калькулятор")
        self.okno.geometry("375x667")
        self.okno.wm_attributes('-topmost', 1)
        self.okno.resizable(0, 0)


        self.total_expretion = ''
        self.current_expretion = ''


        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", " - ": " - ", " + ": " + "}

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_buttons_frame()
        self.create_buttons_digits()
        self.total_l = self.create_total_l()
        self.current_label = self.create_current_l()
        self.create_operations()
        self.create_button_ravno()
        self.create_button_stiranye()

        self.button_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.button_frame.rowconfigure(i, weight=1)
            self.button_frame.columnconfigure(i, weight=1)

    def create_display_frame(self):
        frame = tkinter.Frame(self.okno, height=221, bg='purple')
        frame.pack(expand=True, fill='both')

        return frame


    def create_buttons_frame(self):
        frame = tkinter.Frame(self.okno, bg='white')
        frame.pack(expand=True, fill='both')
        return frame



    def create_button_ravno(self):
        button = tkinter.Button(self.button_frame, text='=', font=("Arial", 20, ), borderwidth=0, bg='lightblue', command=self.ravno)
        button.grid(row=4, column=3, columnspan=2, sticky=tkinter.NSEW)

    def ravno(self):
        self.total_expretion +=  self.current_expretion
        try:
            self.current_expretion = (str(eval(self.total_expretion)))
            self.update_current_lable()
            self.update_total_lable()
            self.total_expretion = ''
        except:
            self.current_expretion = "Error"
            self.update_current_lable()
            self.update_total_lable()
            self.total_expretion = ''
            self.current_expretion = ''










    def C(self):

        self.total_expretion = ''
        self.current_expretion = ''
        self.update_total_lable()
        self.update_current_lable()




    def create_button_stiranye(self):
        button = tkinter.Button(self.button_frame, text='C', font=("Arial", 20, ), borderwidth=0, bg='lightblue', command=self.C)
        button.grid(row=0, columnspan=3, column=1, sticky=tkinter.NSEW)



    def create_buttons_digits(self):
        for value, grid_value in self.digits.items():
            button = tkinter.Button(self.button_frame, text=value, font=("Arial", 20 , 'bold'), borderwidth=0, bg='lightblue', command=lambda x=value: self.add_digits(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tkinter.NSEW)


    def add_digits(self, digit):
        self.current_expretion += (str(digit))
        self.update_current_lable()

#current=низ
#total=вверх
    def add_operations(self, operations):
        self.current_expretion += operations
        self.total_expretion = self.current_expretion
        self.current_expretion = ''
        self.update_current_lable()
        self.update_total_lable()




    def create_operations(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tkinter.Button(self.button_frame, text=symbol, font=("Arial", 15, 'bold'), borderwidth=0,
                                    bg='lightblue', command=lambda y=operator: self.add_operations(y))
            button.grid(row=i, column=4, sticky=tkinter.NSEW)
            i += 1


#expretion = code
#lable = visual
    def create_total_l(self):
        lable = tkinter.Label(self.display_frame, text=self.total_expretion, bg='white', font=('Arial', 15), anchor=tkinter.E, padx=22)
        lable.pack(expand=True, fill='both')
        return lable

    def create_current_l(self):
        lable = tkinter.Label(self.display_frame, text=self.current_expretion, bg='white', font=('Arial', 25),  padx=22, anchor=tkinter.E)
        lable.pack(expand=True, fill='both')
        return lable

    def update_total_lable(self):
        p_tl = self.total_expretion
        p_tl = p_tl.replace("/", " \u00F7 ").replace('*', ' \u00D7 ')
        self.total_l.config(text=p_tl)


    def update_current_lable(self):
        self.current_label.config(text=self.current_expretion)


    def start_loop(self):
        self.okno.mainloop()


if __name__ == '__main__':
    calc = Calc()
    calc.start_loop()

