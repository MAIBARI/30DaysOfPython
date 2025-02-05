import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print(f"Failed to get weather data for {city}. Error code: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = ""  # Replace with your actual API key
    get_weather(city, api_key)
    