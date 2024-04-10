from tkinter import Tk, ttk

from app.main_menu.services import calculate_root_geometry
from app.calculator.main import start_calculator


class MainMenu(Tk):
    widgets_settings = {
        "welcome_label": {
            "font": ("Georgia", 22),
            "text": "Welcome to Personal Helper!",
            "anchor": "n",
            "pady": 30,
        },
        "menu_button": {
            "pady": 30,
            "font": ("Georgia", 20)
        },
        "calculator_button": {
            "text": "Calculator",
        },
        "weather_button": {
            "text": "Check Weather",
        },
        "exit_button": {
            "text": "Leave",
            "pady": 30,
            "side": "bottom"
        },
    }

    def __init__(self):
        super().__init__()
        self.title("Personal Helper")
        self.geometry(calculate_root_geometry(self))
        self.resizable(False, False)
        self.create_widgets()
        self.make_binds()

    def create_widgets(self):
        # Make styles and settings for menu buttons
        menu_button_style = ttk.Style()
        menu_button_style.configure("Menu.TButton", font=MainMenu.widgets_settings["menu_button"]["font"])

        # Settings for welcome label
        welcome_label_config = MainMenu.widgets_settings['welcome_label']
        welcome_label = ttk.Label(self, text=welcome_label_config['text'], font=welcome_label_config['font'])
        welcome_label.pack(anchor=welcome_label_config['anchor'], pady=welcome_label_config["pady"])

        # Settings for "Calculator" button
        calculator_button_config = MainMenu.widgets_settings["calculator_button"]
        calculator_button = ttk.Button(self, text=calculator_button_config["text"], style="Menu.TButton", command=start_calculator)
        calculator_button.pack(pady=MainMenu.widgets_settings["menu_button"]["pady"])

        # Settings for "Weather" button
        weather_button_config = MainMenu.widgets_settings["weather_button"]
        weather_button = ttk.Button(self, text=weather_button_config["text"], style="Menu.TButton")
        weather_button.pack(pady=MainMenu.widgets_settings["menu_button"]["pady"])

        # Settings for "Exit" button
        exit_button_config = MainMenu.widgets_settings["exit_button"]
        exit_button = ttk.Button(self, text=exit_button_config["text"], style="Menu.TButton", command=self.destroy)
        exit_button.pack(pady=MainMenu.widgets_settings["exit_button"]["pady"],
                         side=MainMenu.widgets_settings["exit_button"]["side"])

    def make_binds(self):
        # Bind exit on Esc
        self.bind("<Escape>", lambda event: self.destroy())

    def start(self):
        self.mainloop()
