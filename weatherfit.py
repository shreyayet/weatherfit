import requests
import tkinter as tk
from tkinter import messagebox

# Your API key
api_key = "2c5f94e53931693d22cd452c2678ed8e"  # ← Replace this with your real API key

# Function to get weather and suggest outfit
def get_weather():
    city = city_entry.get()

    if not city:
        messagebox.showerror("Error", "Please enter a city.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            result = f"🌡️ {temp}°F\n☁️ {description.title()}\n💨 Wind: {wind_speed} mph\n\n"

            # Outfit suggestions
            if temp < 40:
                result += "It's cold! 🥶 Bring a coat before you head out!"
            elif 40 <= temp < 55:
                if "wind" in description or wind_speed > 20:
                    result += "It’s chilly and windy! 🌬️ Try pairing jeans with a sweater - layer up!"
                else:
                    result += "It's a bit chilly! Wear a sweater or light jacket with jeans or leggings. Bring layers just in case. If you want to be comfy, wear a sweat set! "
            elif 55 <= temp < 70:
                result += "It's nice out! 🌤️ Bring a light jacket or wear a long sleeve shirt for when it get's cooler later."
            elif 70 <= temp < 80:
                result += "It’s warm! 🌞 Wear a flowy dress today! Or a cute shirt and shorts."
            else:
                result += "It’s hot! 🍳 Go for light fabrics — tank tops, dresses, or athletic wear."

            if "sun" in description or "clear" in description:
                result += "And the sun is out today — bring sunnies and don't forget sunscreen! 😎"

            output_label.config(text=result)

        else:
            messagebox.showerror("Error", f"Could not get weather for '{city}'. Please try again!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("WeatherFit ☁️")

# City input
city_label = tk.Label(root, text="Enter your city:")
city_label.pack(pady=(10, 0))

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=(0, 10))

# Get Weather button
get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack()

# Output label
output_label = tk.Label(root, text="", justify="left", wraplength=300)
output_label.pack(padx=10, pady=15)

# Run the GUI app
root.mainloop()