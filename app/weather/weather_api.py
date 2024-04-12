import requests


class WeatherAPI:
    api_key = ""
    city = "Stockholm"

    def get_weather_forecast(self):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={WeatherAPI.city}&appid={WeatherAPI.api_key}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                forecast_data = response.json()
                return forecast_data
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def create_weather_api():
        return WeatherAPI()