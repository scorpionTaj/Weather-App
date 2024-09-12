from tkinter import *
import os
import requests
from dotenv import load_dotenv

load_dotenv()

object_root = Tk()
object_root.geometry("800x2060")
object_root.title("Weather App - Tajeddine")


headingLabel = Label(
    object_root, text="Welcome To The Weather App ", fg="blue", font="Algerian 20 bold"
)
headingLabel.pack()


searchCityLabel = Label(
    object_root, text="Search City ", fg="dark blue", font="Ariel 14 "
)
searchCityLabel.pack()

canvas1 = Canvas(object_root, width=400, height=800)
canvas1.pack()

entry1 = Entry(object_root)
canvas1.create_window(200, 30, window=entry1)


def getWeather():
    api_key = os.getenv("WEATHER_API_KEY")

    city = entry1.get()
    url = (
        "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + city
    )
    data = requests.get(url).json()

    if data["cod"] != "404":
        y = data["main"]

    current_temperature = y["temp"]
    current_temperature -= 274.04

    current_pressure = y["pressure"]
    current_pressure *= 0.0009869233

    current_humidity = y["humidity"]

    z = data["weather"]
    weather_description = z[0]["description"]

    degree_sign = "\N{DEGREE SIGN}"

    temperature = "{:.0f}".format(current_temperature) + degree_sign + "C"
    pressure = "{:.0f}".format(current_pressure) + " atm"
    humidity = str(current_humidity) + "%"
    details = weather_description

    labelCity = Label(
        object_root,
        text="Currently in " + city.upper(),
        fg="purple",
        font="poppins 15 ",
    )
    canvas1.create_window(200, 180, window=labelCity)

    labelTemperature = Label(
        object_root,
        text="Temperature: " + temperature + ", " + details,
        fg="purple",
        font="poppins 15",
    )
    canvas1.create_window(200, 240, window=labelTemperature)

    labelPressure = Label(
        object_root, text="Pressure: " + pressure, fg="purple", font="poppins 15 "
    )
    canvas1.create_window(200, 300, window=labelPressure)

    labelHumidity = Label(
        object_root, text="Humidity: " + humidity, fg="purple", font="poppins 15 "
    )
    canvas1.create_window(200, 360, window=labelHumidity)

    footer = Label(object_root, text="By ScorpionTaj")
    canvas1.create_window(200, 500, window=footer)


button1 = Button(text="Search", command=getWeather, bg="black", fg="white")
canvas1.create_window(200, 80, window=button1)

object_root.mainloop()
