from tkinter import *
from main import get_weather_data

THEME_COLOR = "#d6f1ff"
FONT_NAME = "Courier"


def forecast():
    city = city_name_entry.get()
    if city == "":
        pass
    else:
        data = get_weather_data(city)
        description_display.config(text=data["description"])
        if data.get('temperature'):
            temperature_display.config(text=f"{data['temperature']}°C")
        if data.get('windspeed'):
            windspeed_display.config(text=f"{data['windspeed']}m/s")
        if data.get('humidity'):
            humidity_display.config(text=f"{data['humidity']}%")


window = Tk()
window.title("WEATHER FORECAST APP")
window.config(padx=20, pady=20, bg=THEME_COLOR)

title_label = Label(text="WEATHER FORECAST APP", bg=THEME_COLOR, fg="#16018a", font=(FONT_NAME, 50))
title_label.pack(pady=15)

city_name_label = Label(text="Enter your city name:", bg=THEME_COLOR, fg="#16018a", font=(FONT_NAME, 20))
city_name_label.place(x=10, y=100)

city_name_entry = Entry(fg="#16018a", width=15, font=(FONT_NAME, 20))
city_name_entry.place(x=300, y=100)

get_weather_button = Button(text="Get Weather", fg="#16018a", font=(FONT_NAME, 20), command=forecast)
get_weather_button.place(x=190, y=150)

description_label = Label(text="Description: ", bg=THEME_COLOR, fg="#16018a", font=(FONT_NAME, 20))
description_label.place(x=10, y=225)

description_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
description_display.place(x=200, y=225)

temperature_img = PhotoImage(file="images/temperature.png")
temperature_label = Label(image=temperature_img, bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
temperature_label.place(x=10, y=275)

temperature_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
temperature_display.place(x=15, y=375)

windspeed_img = PhotoImage(file="images/windspeed.png")
windspeed_label = Label(image=windspeed_img, bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
windspeed_label.place(x=220, y=275)

windspeed_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
windspeed_display.place(x=235, y=375)

humidity_img = PhotoImage(file="images/humidity.png")
humidity_label = Label(image=humidity_img, bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
humidity_label.place(x=430, y=275)

humidity_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
humidity_display.place(x=460, y=375)

window.geometry("+450+125")
window.minsize(width=270, height=500)
window.resizable(False, False)
window.mainloop()