from tkinter import Tk, ttk

from app.weather.weather_api import WeatherAPI


class Weather(Tk):
    weather_api = WeatherAPI.create_weather_api()

    def __init__(self):
        super().__init__()
        self.title("Weather")
        self.geometry("800x700")
        self.resizable(False, False)

        self.make_binds()
        self.create_widgets()

    def create_widgets(self):
        weather_report = Weather.weather_api.get_weather_report()
        for index, (city, weather_report) in enumerate(weather_report.items()):
            city_label = ttk.Label(self, text=city, font=("Georgia", 18, "bold"))
            city_label.grid(row=index, column=0, padx=20, pady=80, sticky="w")

            weather_label = ttk.Label(
                self,
                text=weather_report,
                wraplength=300,
                justify="left",
                font=("Georgia", 12),
            )
            weather_label.grid(row=index, column=1, padx=50, pady=50, sticky="w")

            self.grid_columnconfigure(1, weight=1)

    def make_binds(self):
        # Bind exit on Esc
        self.bind("<Escape>", lambda event: self.destroy())


def start_weather():
    weather = Weather()
