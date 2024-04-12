from tkinter import Tk, ttk

from app.weather.weather_api import WeatherAPI


class Weather(Tk):
    weather_api = WeatherAPI.create_weather_api()

    def __init__(self):
        super().__init__()
        self.title("Weather Forecast")
        self.geometry("800x600")
        self.resizable(False, False)

        self.create_widgets()
        self.make_binds()

    def create_widgets(self):
        forecast_data = Weather.weather_api.get_weather_forecast()
        if isinstance(forecast_data, dict):
            city_label = ttk.Label(self, text=f"Weather Forecast for {WeatherAPI.city}", font=("Georgia", 18, "bold"))
            city_label.pack(pady=20)

            for day in forecast_data["list"][:3]:
                date_time = day["dt_txt"]
                temperature = day["main"]["temp"]
                weather_description = day["weather"][0]["description"]

                forecast_text = f"{date_time}\nTemperature: {temperature}°C\nDescription: {weather_description}"

                forecast_label = ttk.Label(self, text=forecast_text, wraplength=600, font=("Georgia", 12))
                forecast_label.pack(pady=20)

    def make_binds(self):
        # Bind exit on Esc
        self.bind("<Escape>", lambda event: self.destroy())


def start_weather():
    weather = Weather()
