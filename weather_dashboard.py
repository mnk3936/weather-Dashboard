import requests

# Constants
API_KEY = 'dc6c881f7090d1956c59c85b0a8bef3d'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        # Make a request to the OpenWeatherMap API
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Extract relevant data
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display the weather details
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except KeyError:
        print("City not found. Please check the city name and try again.")

def main():
    print("Welcome to the Weather Dashboard!")
    while True:
        city = input("Enter the name of the city (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        get_weather(city)

if __name__ == '__main__':
    main()
