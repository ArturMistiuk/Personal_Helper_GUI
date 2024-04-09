from tkinter import Tk
from tkinter import ttk

from app.main_menu.services import calculate_root_geometry


class MainMenu:

    title = 'Personal Helper'

    def __init__(self, root: Tk):
        self.root = root
        self.root.title(MainMenu.title)
        self.root.geometry(calculate_root_geometry(self.root))
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        welcome_label = ttk.Label(text="Welcome to Personal Helper!",  font=("Arial", 14))
        welcome_label.pack(anchor='n', pady=30)

    def start(self):
        self.root.mainloop()
