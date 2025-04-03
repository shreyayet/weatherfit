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


# Outfit suggestion logic
print("\nHere's what you should wear:")

if temp < 40:
    print("It's chilly! 🥶 Wear a coat before you leave.")
elif 40 <= temp < 55:
    if "wind" in description or wind_speed > 20:
        print("It's chilly and windy. 🌬️ Try pairing jeans with a sweater today, or wear a matching sweat set.")
    else: 
        print("Pair jeans with a light sweater or cardigan. Layer up just in case!")
elif 55 <= temp < 70:
    print("It's nice out!🌤️ But layer up to be safe, a light jacket/sweater or long-sleeve shirt should do the trick.")
elif 70 <= temp < 80:
    print("It's warm! 🌞 The perfect day for a flowy dress.")
else: 
    print("It's hot! 🍳 Stay cool and wear shorts and a tank top.")

# Extra tip if the sun is out
if "sun" in description or "clear" in description:
    print("☀️ And it's sunny! Bring sunnies & don't forget sunscreen.")