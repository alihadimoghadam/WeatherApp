import requests
import json
import tkinter as tk

def fetch_weather_data(city):
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return None


def display_weather(data):
    if not data or data["cod"] != 200:
        result_label.config(text="City not found.")
    else:
        city = data["name"]
        weather = data["weather"][0]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = weather["description"]

        result = f"Weather in {city}:\n"
        result += f"Temperature: {temperature}°C\n"
        result += f"Humidity: {humidity}%\n"
        result += f"Weather Description: {weather_description}"
        result_label.config(text=result)


def get_weather():
    city = city_entry.get()
    weather_data = fetch_weather_data(city)
    display_weather(weather_data)

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create the widgets
city_label = tk.Label(window, text="Enter a city name:")
city_entry = tk.Entry(window)
units_label = tk.Label(window, text="Choose units:")
units_var = tk.IntVar(value=1)
celsius_radio = tk.Radiobutton(window, text="Celsius", variable=units_var, value=1)
fahrenheit_radio = tk.Radiobutton(window, text="Fahrenheit", variable=units_var, value=2)
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
result_label = tk.Label(window, wraplength=300)

# Place the widgets on the window
city_label.pack()
city_entry.pack()
units_label.pack()
celsius_radio.pack()
fahrenheit_radio.pack()
get_weather_button.pack()
result_label.pack()

# Start the GUI event loop
window.mainloop()
