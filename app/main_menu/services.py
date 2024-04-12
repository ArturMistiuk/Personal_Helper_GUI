from tkinter import Tk


def calculate_root_geometry(root: Tk) -> str:
    # Screen sizes
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Main menu window sizes
    window_width = 900
    window_height = 700

    # Coordinates for screen center
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Setup a window
    main_menu_geometry = f"{window_width}x{window_height}+{x_position}+{y_position}"

    return main_menu_geometry
