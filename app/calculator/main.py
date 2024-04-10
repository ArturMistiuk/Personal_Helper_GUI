from tkinter import Tk
from tkinter import ttk


class Calculator(Tk):
    buttons = [
        '%', 'C', 'del', '/',
        '1', '2', '3', '*',
        '4', '5', '6', '+',
        '7', '8', '9', '-',
        '.', '0', 'X^2', '2√', '='
    ]

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)

        self.formula = ''
        self.expression_label = ttk.Label(self, text=self.formula, font=('Georgia', 20), anchor='e', relief='sunken',
                                          borderwidth=2)
        self.expression_label.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=10, padx=10)

        self.create_widgets()
        self.make_binds()

    def create_widgets(self):
        # Create and place all the buttons
        max_cols = 4
        num_rows = 5

        for i, button_text in enumerate(Calculator.buttons):
            row = 1 + i // max_cols
            col = i % max_cols
            get_label = lambda text=button_text: self.calculate(text)
            button = ttk.Button(self, text=button_text, command=get_label)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            self.grid_rowconfigure(row, weight=1)
            self.grid_columnconfigure(col, weight=1)

        # Special placement for certain buttons
        self.special_button_placement(num_rows)

    def special_button_placement(self, num_rows):
        # Place the "." button
        decimal_button = [button for button in self.children.values() if button.cget('text') == '.'][0]
        decimal_button.grid(row=num_rows, column=0, sticky="nsew", padx=5, pady=5, ipadx=5, ipady=5)

        # Place the "0" button
        null_button = [button for button in self.children.values() if button.cget('text') == '0'][0]
        null_button.grid(row=num_rows, column=1, padx=5, pady=5, sticky="nsew", ipadx=5, ipady=5)  # Wider zero button

        # Place the "=" button
        equals_button = [button for button in self.children.values() if button.cget('text') == '='][0]
        equals_button.grid(row=num_rows, column=2, columnspan=2, sticky="nsew", padx=5, pady=5, ipadx=20, ipady=10)

        # Place the "X^2" button
        square_button = [button for button in self.children.values() if button.cget('text') == 'X^2'][0]
        square_button.grid(row=num_rows + 1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5, ipadx=20, ipady=10)

        # Place the "2√" button
        root_button = [button for button in self.children.values() if button.cget('text') == '2√'][0]
        root_button.grid(row=num_rows + 1, column=2, columnspan=2, sticky="nsew", padx=5, pady=5, ipadx=20, ipady=10)

    def make_binds(self):
        # Bind exit on Esc
        self.bind("<Escape>", lambda event: self.destroy())

    def calculate(self, operation):
        if operation == 'C':
            self.formula = ''
        elif operation == 'del':
            self.formula = self.formula[:-1]  # Remove last character
        elif operation == 'X^2':
            try:
                self.calculate("=")  # Calculate before square to avoid error
                result = float(self.formula) ** 2
                self.formula = str(result)
            except ValueError:
                self.formula = 'Error'
        elif operation == '2√':
            try:
                self.calculate("=")  # Calculate before root to avoid error
                result = float(self.formula) ** 0.5
                self.formula = str(result)
            except ValueError:
                self.formula = 'Error'
        elif operation == '%':
            try:
                self.calculate("=")  # Calculate before root to avoid error
                result = float(self.formula) / 100
                self.formula = str(result)
            except ValueError:
                self.formula = 'Error'
        elif operation == '=':
            try:
                result = eval(self.formula)
                self.formula = str(result)
            except Exception:
                self.formula = 'Error'
        else:
            if self.formula == '0':
                self.formula = ''  # Clear '0' before adding new digit or operation
            self.formula += operation

        self.expression_label.configure(text=self.formula)


def start_calculator():
    calculator = Calculator()
