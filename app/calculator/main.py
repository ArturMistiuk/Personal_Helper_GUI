from tkinter import ttk, Tk


class Calculator(Tk):
    buttons = [
        '%', 'C', 'del', '/',
        '1', '2', '3', '*',
        '4', '5', '6', '+',
        '7', '8', '9', '-',
        'X^2', '0', '2√', '='
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
        for i, button_text in enumerate(Calculator.buttons):
            row = 1 + i // 4
            col = i % 4
            get_label = lambda text=button_text: self.calculate(text)
            button = ttk.Button(self, text=button_text, command=get_label)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            self.grid_rowconfigure(row, weight=1)
            self.grid_columnconfigure(col, weight=1)

    def calculate(self, operation):
        if operation == 'C':
            self.formula = ''
        elif operation == 'del':
            self.formula = self.formula[0:-1]
        elif operation == 'X^2':
            try:
                self.calculate("=")    # Calculate before square to aviod error
                result = float(self.formula) ** 2
                self.formula = str(result)
            except ValueError:
                self.formula = 'Error'
        elif operation == "2√":
            try:
                self.calculate("=")    # Calculate before root to aviod error
                result = float(self.formula) ** 0.5
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
                self.formula = ''
            self.formula += operation

        self.expression_label.configure(text=self.formula)

    def make_binds(self):
        # Bind exit on Esc
        self.bind("<Escape>", lambda event: self.destroy())


def start_calculator():
    calculator = Calculator()
