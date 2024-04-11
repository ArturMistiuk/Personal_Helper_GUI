import tkinter as tk
from tkinter import ttk, messagebox
import json


class WaterBalance(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Daily Water Balance")

        self.default_weight = tk.StringVar(value="80")
        self.default_height = tk.StringVar(value="180")
        self.water_var = tk.StringVar(value="0")

        self.load_data()
        self.create_widgets()
        self.make_binds()

    def load_data(self):
        try:
            with open("water_balance_data.json", "r") as file:
                data = json.load(file)
                self.default_weight.set(str(data.get("weight")))
                self.default_height.set(str(data.get("height")))
                self.water_var.set(str(data.get("water_drunk")))
        except FileNotFoundError:
            # If data file is not found, use default values
            pass

    def save_data(self):
        data = {
            "weight": float(self.default_weight.get()),
            "height": float(self.default_height.get()),
            "water_drunk": float(self.water_var.get())
        }
        with open("water_balance_data.json", "w") as file:
            json.dump(data, file)

    def calculate_water_requirement(self):
        try:
            weight = float(self.default_weight.get())
            height = float(self.default_height.get()) / 100

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                water_requirement = weight * 40
            elif 18.5 <= bmi < 25:
                water_requirement = weight * 35
            else:
                water_requirement = weight * 30

            water_requirement_liters = water_requirement / 1000
            self.water_requirement_label.config(
                text=f"Recommended water intake per day: {water_requirement_liters:.2f} L")

            self.save_data()  # Save data after calculation
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data")

    def update_water_balance(self):
        try:
            water_drunk = float(self.water_var.get())
            water_required = float(self.water_requirement_label.cget("text").split(": ")[1].split(" ")[0])

            remaining_water = water_required - water_drunk
            messagebox.showinfo("Water Balance", f"Remaining water requirement for the day: {remaining_water:.2f} L")

            self.save_data()  # Save data after updating water balance
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid water amount")

    def create_widgets(self):
        menu_button_style = ttk.Style()
        menu_button_style.configure(
            "Water.TButton", font=("Georgia", 12)
        )

        input_frame = ttk.Frame(self, padding="20")
        input_frame.pack(fill=tk.BOTH, expand=True)

        weight_label = ttk.Label(input_frame, text="Enter your weight (kg):")
        weight_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        weight_entry = ttk.Entry(input_frame, textvariable=self.default_weight)
        weight_entry.grid(row=0, column=1, padx=10, pady=10)

        height_label = ttk.Label(input_frame, text="Enter your height (cm):")
        height_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        height_entry = ttk.Entry(input_frame, textvariable=self.default_height)
        height_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = ttk.Button(input_frame, text="Calculate", command=self.calculate_water_requirement, style="Water.TButton")
        calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.water_requirement_label = ttk.Label(input_frame, text="")
        self.water_requirement_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        water_entry_label = ttk.Label(input_frame, text="Enter amount of water consumed (L):")
        water_entry_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        water_entry = ttk.Entry(input_frame, textvariable=self.water_var)
        water_entry.grid(row=4, column=1, padx=10, pady=10)

        update_button = ttk.Button(input_frame, text="Update Balance", command=self.update_water_balance, style="Water.TButton")
        update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def make_binds(self):
        # Bind exit on Esc
        self.bind("<Escape>", lambda event: self.withdraw())


water_balance = WaterBalance()
water_balance.withdraw()


def start_water_balance():
    water_balance.deiconify()
