import requests
city = input("Enter your city: ")
api_key = "2c5f94e53931693d22cd452c2678ed8e"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

# Making a GET request to the OpenWeatherMap API
response = requests.get(url)

# Converting the response to JSON format (dictionary format)
data = response.json()

# Print out the temperature and weather description
if response.status_code == 200:
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    print(f"\nWeather in {city.title()}:")
    print (f"Temperature: {temp}°F")
    print (f"Condition: {description}")
    print (f"Wind Speed: {wind_speed} mph")
else:
    print("\nSorry! The weather for that city is unavailable. Please try again!")