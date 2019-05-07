import tkinter as tk
import requests
from tkinter import font

Height = 600
Width = 600

# api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml CITY NAME
#4dc29810ecf0e9e9cdf1b447d87353a9  KEY


def real_format_response(weather):
    #print(weather)
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_string = 'City: ' + str(name) + '\n'  + 'Description: ' + str(description) + '\n' + 'Temperature: ' + str(temperature) + ' °F'
    except:
        final_string = "Oooops! Invalid Input, Try Again"
    return final_string

def get_weather(city):
    weather_key = "4dc29810ecf0e9e9cdf1b447d87353a9"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text']= real_format_response(weather)

    
root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

'''
bg_image = tk.PhotoImage(file='download.jpeg')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
'''


frame1 = tk.Frame(root, bg="purple", bd=5)    #80cffc
frame1.place(relwidth=0.75, relheight=0.10, relx=0.5, rely=0.10, anchor='n')

entry = tk.Entry(frame1, font=('courier', 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame1, font=('courier', 18), text='Weather', fg="white", bg="green", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.30)

frame2 = tk.Frame(root, bg="purple", bd=5)
frame2.place(relwidth=0.75, relheight=0.70, relx=0.5, rely=0.20, anchor='n')

label = tk.Label(frame2, fg="red", font=('Modern', 25), bg="black", text="Weather Results Board", anchor='nw', justify='left', border=30)
label.place(relwidth=1, relheight=1)

'''
label = tk.Label(frame1, text="Password Needed", bg="grey", fg="yellow")
label.place(relx=0, rely=0, relheight=0.2, relwidth=0.25)

entry = tk.Entry(frame1)
entry.place(relx=0.30, rely=0, relheight=0.2, relwidth=0.40)

button = tk.Button(frame1, text="Login", bg="red", fg="white")
button.place(relx=0.75, rely=0, relheight=0.2, relwidth=30)
'''

root.mainloop()
