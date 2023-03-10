import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator")

        self.equation = tk.StringVar()
        self.equation.set("0")

        self.display = tk.Entry(master, textvariable=self.equation, justify="right")
        self.display.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

        # Tombol-tombol
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)
        self.create_button(".", 4, 2)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        self.create_button("Del", 4, 0)
        self.create_button("C", 5, 0)
        self.create_button("=", 5, 2)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=8, height=4, command=lambda: self.click(text))
        button.grid(row=row, column=column, padx=8, pady=8)

    def click(self, text):
        if text == "C":
            self.equation.set("0")
        elif text == "Del":
            self.equation.set(self.equation.get()[:-1])
        elif text == "=":
            try:
                self.equation.set(eval(self.equation.get()))
            except:
                self.equation.set("Error")
        else:
            if self.equation.get() == "0":
                self.equation.set(text)
            else:
                self.equation.set(self.equation.get() + text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
