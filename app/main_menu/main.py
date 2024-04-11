from tkinter import Tk, ttk

from app.calculator.main import start_calculator
from app.main_menu.services import calculate_root_geometry
from app.weather.main import start_weather
from app.water_balance.water_balance import start_water_balance


class MainMenu(Tk):
    widgets_settings = {
        "welcome_label": {
            "font": ("Impact", 30),    # Comic Sans MS / Courier New / Garamond
            "text": "Welcome to Personal Helper!",
            "anchor": "n",
            "pady": 30,
            "background": "#f9f4e6",
            "foreground": "#5b5643",
        },
        "menu_button": {"pady": 30, "font": ("Georgia", 20)},
        "calculator_button": {
            "text": "Calculator",
        },
        "weather_button": {
            "text": "Check Weather",
        },
        "water_balance_button": {
            "text": "Water Balance",
        },
        "exit_button": {"text": "Leave", "pady": 30, "side": "bottom"},
    }

    def __init__(self):
        super().__init__()
        self.title("Personal Helper")
        self.geometry(calculate_root_geometry(self))
        self.resizable(False, False)
        self.create_widgets()
        self.make_binds()
        self.configure(background="#f9f4e6")  # FFF0F5

    def create_widgets(self):
        """
        The create_widgets function creates all the widgets for the main menu.
        It uses a dictionary of dictionaries to store settings for each widget,
        and then it applies those settings when creating each widget.

        :param self: Access the attributes and methods of the class
        :return: None
        :doc-author: Trelent
        """
        menu_button_style = ttk.Style()
        menu_button_style.configure(
            "Menu.TButton", font=MainMenu.widgets_settings["menu_button"]["font"]
        )

        # Settings for welcome label
        welcome_label_config = MainMenu.widgets_settings["welcome_label"]
        welcome_label = ttk.Label(
            self,
            text=welcome_label_config["text"],
            font=welcome_label_config["font"],
            background=welcome_label_config["background"],
            foreground=welcome_label_config["foreground"],
        )
        welcome_label.pack(
            anchor=welcome_label_config["anchor"], pady=welcome_label_config["pady"]
        )

        # Settings for "Calculator" button
        calculator_button_config = MainMenu.widgets_settings["calculator_button"]
        calculator_button = ttk.Button(
            self,
            text=calculator_button_config["text"],
            style="Menu.TButton",
            command=start_calculator,
        )
        calculator_button.pack(pady=MainMenu.widgets_settings["menu_button"]["pady"])

        # Settings for "Weather" button
        weather_button_config = MainMenu.widgets_settings["weather_button"]
        weather_button = ttk.Button(
            self,
            text=weather_button_config["text"],
            style="Menu.TButton",
            command=start_weather,
        )
        weather_button.pack(pady=MainMenu.widgets_settings["menu_button"]["pady"])

        # Settings for "Water Balance" button
        water_balance_button_config = MainMenu.widgets_settings["water_balance_button"]
        water_balance_button = ttk.Button(
            self,
            text=water_balance_button_config["text"],
            command=start_water_balance,
            style="Menu.TButton",
        )
        water_balance_button.pack(pady=MainMenu.widgets_settings["menu_button"]["pady"])

        # Settings for "Exit" button
        exit_button_config = MainMenu.widgets_settings["exit_button"]
        exit_button = ttk.Button(
            self,
            text=exit_button_config["text"],
            style="Menu.TButton",
            command=self.destroy,
        )
        exit_button.pack(
            pady=MainMenu.widgets_settings["exit_button"]["pady"],
            side=MainMenu.widgets_settings["exit_button"]["side"],
        )

    def make_binds(self):
        """
        The make_binds function is a function that binds the escape key to the destroy method.
        This means that when you press escape, it will close the window.

        :param self: Represent the instance of the object itself
        :return: A key binding
        :doc-author: Trelent
        """
        # Bind exit on Esc
        self.bind("<Escape>", lambda event: self.destroy())

    def start(self):
        """
        The start function is the main loop of the game. It calls all other functions in order to run the game.

        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        self.mainloop()
