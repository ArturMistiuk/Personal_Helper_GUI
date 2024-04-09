from tkinter import Tk
from app.main_menu.main import MainMenu

if __name__ == "__main__":
    root = Tk()
    main_menu = MainMenu(root)
    main_menu.start()
