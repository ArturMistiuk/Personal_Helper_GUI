from tkinter import Tk, ttk
from app.main_menu.services import calculate_root_geometry


class MainMenu:
    title = 'Personal Helper'
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

    def __init__(self, root: Tk):
        self.root = root
        self.root.title(MainMenu.title)
        self.root.geometry(calculate_root_geometry(self.root))
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Make styles and settings for menu buttons
        menu_button_style = ttk.Style()
        menu_button_style.configure("Menu.TButton", font=MainMenu.widgets_settings["menu_button"]["font"])

        # Settings for welcome label
        welcome_label_config = MainMenu.widgets_settings['welcome_label']
        welcome_label = ttk.Label(self.root, text=welcome_label_config['text'], font=welcome_label_config['font'])
        welcome_label.pack(anchor=welcome_label_config['anchor'], pady=welcome_label_config["pady"])

        # Settings for "Calculator" button
        calculator_button_config = MainMenu.widgets_settings["calculator_button"]
        calculator_button = ttk.Button(self.root, text=calculator_button_config["text"], style="Menu.TButton")
        calculator_button.pack(pady=MainMenu.widgets_settings["menu_button"]["pady"])

        # Settings for "Weather" button
        weather_button_config = MainMenu.widgets_settings["weather_button"]
        weather_button = ttk.Button(self.root, text=weather_button_config["text"], style="Menu.TButton")
        weather_button.pack(pady=MainMenu.widgets_settings["menu_button"]["pady"])

        # Settings for "Exit" button
        exit_button_config = MainMenu.widgets_settings["exit_button"]
        exit_button = ttk.Button(self.root, text=exit_button_config["text"], style="Menu.TButton")
        exit_button.pack(pady=MainMenu.widgets_settings["exit_button"]["pady"],
                         side=MainMenu.widgets_settings["exit_button"]["side"])

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    main_menu = MainMenu(root)
    main_menu.start()
