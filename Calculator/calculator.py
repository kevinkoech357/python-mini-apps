#!/usr/bin/env python3

# importing modules
from tkinter import *
from tkinter import ttk

class Calculator:

    calc_default_value = 0.0

    add_trigger = False
    sub_trigger = False
    mult_trigger = False
    div_trigger = False

    def button_press(self, value):

        entry_value = self.number_entry.get()

        entry_value += value

        self.number_entry.delete(0, "end")

        self.number_entry.insert(0, entry_value)

    def is_float(self, user_input):

        try:
            float(user_input)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):

        if self.is_float(str(self.number_entry.get())):
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False

            self.calc_default_value = float(self.entry_value.get())

            if value == "+":
                    self.add_trigger = True
            if value == "-":
                    self.sub_trigger = True
            if value == "*":
                    self.mult_trigger = True
            else:
                    self.div_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self):

            if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:

                    if self.add_trigger:
                        solution = self.calc_default_value + float(self.entry_value.get())
                    elif self.sub_trigger:
                        solution = self.calc_default_value - float(self.entry_value.get())
                    elif self.mult_trigger:
                        solution = self.calc_default_value * float(self.entry_value.get())
                    else:
                        solution = self.calc_default_value / float(self.entry_value.get())

                    self.number_entry.delete(0, "end")
                    self.number_entry.insert(0, solution)

    def __init__(self, root):

        self.entry_value = StringVar(root, value="")

        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)

        self.number_entry.grid(row=0, columnspan=4)

        # ==================================================================
        # FIRST ROW 7 8 9 /
        # ==================================================================
        self.button_7 = ttk.Button(root, text="7",
                command=lambda: self.button_press("7")).grid(row=1, column=0)
        self.button_8 = ttk.Button(root, text="8",
                command=lambda: self.button_press("8")).grid(row=1, column=1)
        self.button_9 = ttk.Button(root, text="9",
                command=lambda: self.button_press("9")).grid(row=1, column=2)
        self.division_button = ttk.Button(root, text="/",
                command=lambda: self.math_button_press("/")).grid(row=1, column=3)

        # ==================================================================
        # SECOND ROW 4 5 6 *
        # ==================================================================
        self.button_4 = ttk.Button(root, text="4",
                command=lambda: self.button_press("4")).grid(row=2, column=0)
        self.button_5 = ttk.Button(root, text="5",
                command=lambda: self.button_press("5")).grid(row=2, column=1)
        self.button_6 = ttk.Button(root, text="6",
                command=lambda: self.button_press("6")).grid(row=2, column=2)
        self.multiply_button = ttk.Button(root, text="*",
                command=lambda: self.math_button_press("*")).grid(row=2, column=3)

        # ==================================================================
        # THIRD ROW 1 2 3 +
        # ==================================================================
        self.button_1 = ttk.Button(root, text="1",
                command=lambda: self.button_press("1")).grid(row=3, column=0)
        self.button_2 = ttk.Button(root, text="2",
                command=lambda: self.button_press("2")).grid(row=3, column=1)
        self.button_3 = ttk.Button(root, text="3",
                command=lambda: self.button_press("3")).grid(row=3, column=2)
        self.addition_button = ttk.Button(root, text="+",
                command=lambda: self.math_button_press("+")).grid(row=3, column=3)

        # ==================================================================
        # FOURTH ROW AC 0 = -
        # ==================================================================
        self.clear_button = ttk.Button(root, text="AC",
                command=lambda: self.button_press("AC")).grid(row=4, column=0)
        self.button_0 = ttk.Button(root, text="0",
                command=lambda: self.button_press("0")).grid(row=4, column=1)
        self.equal_button = ttk.Button(root, text="=",
                command=lambda: self.equal_button_press()).grid(row=4, column=2)
        self.subtraction_button = ttk.Button(root, text="-",
                command=lambda: self.math_button_press("-")).grid(row=4, column=3)

def main():
    root = Tk()
    calculator = Calculator(root)
    
    # Styling modifications
    style = ttk.Style()
    style.configure("TButton",
                    font=("Helvetica", 16),
                    padding=10,
                    foreground="black",
                    background="lightgray")
    style.configure("TEntry",
                    font=("Helvetica", 18),
                    padding=10)

    root.title("Calculator")
    root.geometry("535x500")  # Adjust the window size
    
    root.mainloop()

if __name__ == "__main__":
    main()



