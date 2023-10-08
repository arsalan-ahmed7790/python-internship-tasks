import requests

def fetch_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change units to "imperial" for Fahrenheit.
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(data):
    if data is not None:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_condition = data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("No weather data available.")

def main():
    api_key =  "0f45d12b12ff1b9d3d71df6ae42c1fbc" # Replace with your API key.
    
    print("Welcome to the Weather App!")
    
    while True:
        city = input("Enter a city name or 'quit' to exit: ")
        if city.lower() == "quit":
            print("Exiting the Weather App. Goodbye!")
            break
        
        weather_data = fetch_weather_data(api_key, city)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
