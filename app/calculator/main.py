from tkinter import Tk, ttk


class Calculator(Tk):
    buttons = [
        "%",
        "C",
        "del",
        "/",
        "1",
        "2",
        "3",
        "*",
        "4",
        "5",
        "6",
        "+",
        "7",
        "8",
        "9",
        "-",
        ".",
        "0",
        "X^2",
        "2√",
        "=",
    ]

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)

        self.formula = ""
        self.expression_label = ttk.Label(
            self,
            text=self.formula,
            font=("Georgia", 20),
            anchor="e",
            relief="flat",
            borderwidth=2,
        )
        self.expression_label.grid(
            row=0, column=0, columnspan=4, sticky="nsew", pady=10, padx=10
        )

        self.create_widgets()
        self.make_binds()
        self.make_digits_binds()

    def create_widgets(self):
        """
        The create_widgets function creates all the buttons for the calculator.
        It also places them in their appropriate locations on the grid.


        :param self: Refer to the current instance of the class
        :return: None
        :doc-author: Trelent
        """
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
        """
        The special_button_placement function is used to place the &quot;.&quot;, &quot;0&quot;, and &quot;=&quot; buttons in their
        proper locations. It also places the square root and squared buttons in their proper locations.

        :param self: Refer to the object itself
        :param num_rows: Place the buttons in the correct row
        :return: A list of the special buttons
        :doc-author: Trelent
        """
        # Place the "." button
        decimal_button = [
            button for button in self.children.values() if button.cget("text") == "."
        ][0]
        decimal_button.grid(
            row=num_rows, column=0, sticky="nsew", padx=5, pady=5, ipadx=5, ipady=5
        )

        # Place the "0" button
        null_button = [
            button for button in self.children.values() if button.cget("text") == "0"
        ][0]
        null_button.grid(
            row=num_rows, column=1, padx=5, pady=5, sticky="nsew", ipadx=5, ipady=5
        )  # Wider zero button

        # Place the "=" button
        equals_button = [
            button for button in self.children.values() if button.cget("text") == "="
        ][0]
        equals_button.grid(
            row=num_rows,
            column=2,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
        )

        # Place the "X^2" button
        square_button = [
            button for button in self.children.values() if button.cget("text") == "X^2"
        ][0]
        square_button.grid(
            row=num_rows + 1,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
        )

        # Place the "2√" button
        root_button = [
            button for button in self.children.values() if button.cget("text") == "2√"
        ][0]
        root_button.grid(
            row=num_rows + 1,
            column=2,
            columnspan=2,
            sticky="nsew",
            padx=5,
            pady=5,
            ipadx=5,
            ipady=5,
        )

    def make_binds(self):
        """
        The make_binds function is used to bind the buttons on the calculator to their respective functions.
        The function takes in a parameter of self, which is used as a reference for all other functions within this class.
        The first line of code binds the escape key to close out of the program when pressed. The second line binds
        the return key (enter) with its respective function, calculate(). The third through seventh lines bind each
        of their corresponding keys with their respective functions and operators.

        :param self: Refer to the current instance of a class
        :return: The key bindings for the calculator
        :doc-author: Trelent
        """
        self.bind("<Escape>", lambda event: self.destroy())
        self.bind("<Return>", lambda event: self.calculate("="))
        self.bind("*", lambda event: self.calculate("*"))
        self.bind("/", lambda event: self.calculate("/"))
        self.bind(".", lambda event: self.calculate("."))
        self.bind("+", lambda event: self.calculate("+"))
        self.bind("-", lambda event: self.calculate("-"))
        self.bind("<BackSpace>", lambda event: self.calculate("del"))

    def make_digits_binds(self):
        """
        The make_digits_binds function creates the binds for the 0-9 buttons.
        It takes no arguments and returns nothing. It uses a for loop to iterate through each digit,
        and then it calls self.bind(key, lambda event, key=key: self.calculate(key)) on each iteration of the loop.

        :param self: Allow the function to access the attributes and methods of the class
        :return: A bind for each digit 0-9
        :doc-author: Trelent
        """
        for digit in range(10):
            key = str(digit)
            self.bind(key, lambda event, key=key: self.calculate(key))

    def calculate(self, operation):
        """
        The calculate function is the main function of this program. It takes in an operation, which can be a number or an operator, and performs the appropriate action.

        :param self: Refer to the current object
        :param operation: Determine which operation the user wants to perform
        :return: The result of the formula
        :doc-author: Trelent
        """
        if operation == "C":
            self.formula = ""
        elif operation == "del":
            self.formula = self.formula[:-1]  # Remove last character
        elif operation == "X^2":
            try:
                self.calculate("=")  # Calculate before square to avoid error
                result = float(self.formula) ** 2
                self.formula = str(result)
            except ValueError:
                self.formula = "Error"
        elif operation == "2√":
            try:
                self.calculate("=")  # Calculate before root to avoid error
                result = float(self.formula) ** 0.5
                self.formula = str(result)
            except ValueError:
                self.formula = "Error"
        elif operation == "%":
            try:
                self.calculate("=")  # Calculate before root to avoid error
                result = float(self.formula) / 100
                self.formula = str(result)
            except ValueError:
                self.formula = "Error"
        elif operation == "=":
            try:
                result = eval(self.formula)
                self.formula = str(result)
            except Exception:
                self.formula = "Error"
        else:
            if self.formula == "0":
                self.formula = ""  # Clear '0' before adding new digit or operation
            self.formula += operation

        self.expression_label.configure(text=self.formula)


def start_calculator():
    """
    The start_calculator function is the main function of this program. It creates a Calculator object and then calls
    the calculator's run method, which starts the calculator.

    :return: A calculator object
    :doc-author: Trelent"""
    calculator = Calculator()
