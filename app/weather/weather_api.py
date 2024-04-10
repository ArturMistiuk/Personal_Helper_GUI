import requests


class WeatherAPI:
    greeting = "Welcome to the Weather Forecaster!"
    api_key = ''
    cities = ["Stockholm", "Zaporizhzhia", "Warsaw"]
    report = {}

    def get_weather_report(self):
        for city in WeatherAPI.cities:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAPI.api_key}&units=metric'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    weather_data = response.json()
                    weather_description = weather_data['weather'][0]['description']
                    temperature = weather_data['main']['temp']
                    humidity = weather_data['main']['humidity']
                    wind_speed = weather_data['wind']['speed']
                    WeatherAPI.report[city] = (
                    f"Weather report for {city}:\n"
                    f"Description: {weather_description}\n"
                    f"Temperature: {temperature}°C\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind_speed} m/s"
                    )
                else:
                    return f"Error: {response.status_code} - {response.text}"
            except Exception as e:
                return f"Error: {str(e)}"

        return WeatherAPI.report


    @staticmethod
    def create_weather_api():
        return WeatherAPI()





weather_api = WeatherAPI()
weather_report = weather_api.get_weather_report()

print(weather_report)
