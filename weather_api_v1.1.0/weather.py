# Weather API made by Coderorca, V1.0.0
# This file is part of a Free Coding Project and released under the GNU General Public License
# Please consult the license.txt file for more information
# 1.importing the tkinter for GUI
from tkinter import *
import tkinter as tk

# 2. Import packages needed to fetch data
from geopy.geocoders import Nominatim 
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

# 3. Define GUI dimensions and general appearance
root = Tk()
root.title("API Weather App")
root.geometry("1400x650")
root.configure(bg = "#EBBC82")
root.resizable(False, False)

# 3.1 Icon for the window bar
image_icon = PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/logo.png")
root.iconphoto(False, image_icon)

# 3.2 Logo
logo = PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/logo2.png")
logo_icon = Label(image = logo, bg = "#EBBC82")
logo_icon.place(x = 500, y = 125)

# 4. Search bar
search_bar = PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/search_bar.png")
searching = Label(image = search_bar, bg = "#EBBC82")
searching.place(x = 40, y = 40)

# 4.1 Adding a nice deco image
cloud_image = PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/clouds.png")
clouds = Label(root, image = cloud_image, bg = "#42392F")
clouds.place(x = 60, y = 47)

# 5. Main Info Box
# it contains data fetched for the five major points of interests about our weather
# For reference we use the Acronym thpwd
main_infobox = PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/round_rectangle_1.png")
Label(root, image = main_infobox, bg = "#EBBC82").place(x = 40, y = 140)

# 6. The input
textfield = tk.Entry(root, justify = 'left', width = 35, font = ('Calibri', 25, 'bold'), fg = "#FFFFFF", bg = "#42392F", border = 0)
textfield.place(x = 160, y = 52)
textfield.focus()

# 7. Fetching data
def getWeather():
    # User inputs the location name
    city = textfield.get()

    # 7.1 Timezone
    geolocator = Nominatim(user_agent = "geoapiExercise")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    
    # 7.2 Output results
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)

    # 7.3 display the results into the main_infobox
    timezone.config(text = result)
    long_lat.config(text = f"{round(location.latitude,2)}°N, {round(location.longitude,2)}°E")

    # 7.4 pytz to display time and timezones
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text = current_time)

    # 7.5 API Key
    api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=2590e5133cbf22730ec0a8c4825b7906"

    # 7.6 Converting fetched data into json format
    json_data = requests.get(api).json()

    # Note: For experimental purposes the API Key and the One Call Function will be temporarily made available for 
    # evaluation, Mr. Schirmer. After evaluation is done, the API key expires within 24 hours

    # 7.7 Display our thpwd inquiry
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    # 7.8 configuring the results to be displayed into the textfields
    t.config(text = f"{round(temp,1)}°C")
    h.config(text = (humidity, "%"))
    p.config(text = (pressure, "hPa"))
    w.config(text = f"{round(wind,1)}m/s")
    d.config(text = description)

    # 7.9 Referencing the cellblocks in the footer
    # first cell
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']

    photo1 = ImageTk.PhotoImage(file = f"C:/Users/PC-04/Desktop/weather_api_v1.1.0/icon/{firstdayimage}.png")
    firstimage.config(image = photo1)
    firstimage.image = photo1
    firstimage.place (x = 10, y = 50)
    
    # Cell 1
    temppresent = json_data['daily'][0]['temp']['day']
    temppresentnight = json_data['daily'][0]['temp']['night']

    presenttemp.config(font = ("Calibri", 20), text = f"Day: {round(temppresent)} °C\n Night: {round(temppresentnight)} °C")
    
    # Cell 2
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']

    img = (Image.open(f"C:/Users/PC-04/Desktop/weather_api_v1.1.0/icon/{seconddayimage}.png"))

    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image = photo2)
    secondimage.image = photo2
    secondimage.place (x = 15, y = 30)

    tempday1 = json_data['daily'][1]['temp']['day']
    tempnight1 = json_data['daily'][1]['temp']['night']

    day1temp.config(font = ("Calibri", 10), text = f"Day: {round(tempday1)} °C\n Night: {round(tempnight1)} °C")

    # Cell 3
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    img = (Image.open(f"C:/Users/PC-04/Desktop/weather_api_v1.1.0/icon/{thirddayimage}.png"))
    
    resized_image = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image = photo3)
    thirdimage.image = photo3
    thirdimage.place (x = 15, y = 30)

    tempday2 = json_data['daily'][2]['temp']['day']
    tempnight2 = json_data['daily'][2]['temp']['night']

    day2temp.config(font = ("Calibri", 10), text = f"Day: {round(tempday2)} °C\n Night: {round(tempnight2)} °C")

    # Cell 4
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    img = (Image.open(f"C:/Users/PC-04/Desktop/weather_api_v1.1.0/icon/{fourthdayimage}.png"))
    
    resized_image = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image = photo4)
    fourthimage.image = photo4
    fourthimage.place (x = 15, y = 30)

    tempday3 = json_data['daily'][3]['temp']['day']
    tempnight3 = json_data['daily'][3]['temp']['night']

    day3temp.config(font = ("Calibri", 10), text = f"Day: {round(tempday3)} °C\n Night: {round(tempnight3)} °C")

    # Cell 5
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    img = (Image.open(f"C:/Users/PC-04/Desktop/weather_api_v1.1.0/icon/{fifthdayimage}.png"))
    
    resized_image = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image = photo5)
    fifthimage.image = photo5
    fifthimage.place (x = 15, y = 30)

    tempday4 = json_data['daily'][4]['temp']['day']
    tempnight4 = json_data['daily'][4]['temp']['night']

    day4temp.config(font = ("Calibri", 10), text = f"Day: {round(tempday4)} °C\n Night: {round(tempnight4)} °C")

    # Cell 6
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    img = (Image.open(f"C:/Users/PC-04/Desktop/weather_api_v1.1.0/icon/{sixthdayimage}.png"))
    
    resized_image = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image = photo6)
    sixthimage.image = photo6
    sixthimage.place (x = 15, y = 30)

    tempday5 = json_data['daily'][5]['temp']['day']
    tempnight5 = json_data['daily'][5]['temp']['night']

    day5temp.config(font = ("Calibri", 10), text = f"Day: {round(tempday5)} °C\n Night: {round(tempnight5)} °C")

    # Cell 7
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img = (Image.open(f"C:/Users/PC-04/Desktop/weather_api_v1.1.0/icon/{seventhdayimage}.png"))
    
    resized_image = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image = photo7)
    seventhimage.image = photo7
    seventhimage.place (x = 15, y = 30)

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']

    day6temp.config(font = ("Calibri", 10), text = f"Day: {round(tempday6)} °C\n Night: {round(tempnight6)} °C")

    # forecast days
    first = datetime.now()
    present.config(text = first.strftime("%A"))

    second = first+timedelta(days = 1)
    day1.config(text = second.strftime("%A"))

    third = second+timedelta(days = 1)
    day2.config(text = third.strftime("%A"))

    fourth = third+timedelta(days = 1)
    day3.config(text = fourth.strftime("%A"))

    fifth = fourth+timedelta(days = 1)
    day4.config(text = fifth.strftime("%A"))

    sixth = fifth+timedelta(days = 1)
    day5.config(text = sixth.strftime("%A"))

    seventh = sixth+timedelta(days = 1)
    day6.config(text = seventh.strftime("%A"))

# 8. Creating labels for our results. Labels are self-explainatory
temperature = Label(root, text = "Temperature:", font = ('Calibri', 12, 'bold'), fg = "#ffffff", bg = "#42392F")
temperature.place(x = 50, y = 150)

humidity = Label(root, text = "Humidity:", font = ('Calibri', 12, 'bold'), fg = "#ffffff", bg = "#42392F")
humidity.place(x = 50, y = 170)

pressure = Label(root, text = "Pressure:", font = ('Calibri', 12, 'bold'), fg = "#ffffff", bg = "#42392F")
pressure.place(x = 50, y = 190)

wind_speed = Label(root, text = "Wind Speed:", font = ('Calibri', 12, 'bold'), fg = "#ffffff", bg = "#42392F")
wind_speed.place(x = 50, y = 210)

description = Label(root, text = "Description", font = ('Calibri', 12, 'bold'), fg = "#ffffff", bg = "#42392F")
description.place(x = 50, y = 230)

# 9. Send inquiry and display results
search_icon = PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/search_icon.png")
s_icon = Button(image = search_icon, bg = "#42392F", borderwidth = 0, cursor = "hand2", command = getWeather)
s_icon.place(x = 780, y = 48)

# 10. Footer
frame = Frame(root, width = 1400, height = 230, bg = "#42392F")
frame.pack(side = BOTTOM)

# 10.1 Adding Forecast cells
firstbox=PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/round_rectangle_2.png")
secondbox=PhotoImage(file = "C:/Users/PC-04/Desktop/weather_api_v1.1.0/images/round_rectangle_3.png")

# 10.2 Adding boxes for each day
Label(frame, image = firstbox, bg="#42392F").place(x = 40, y = 40)
Label(frame, image = secondbox, bg="#42392F").place(x = 360, y = 40)
Label(frame, image = secondbox, bg="#42392F").place(x = 480, y = 40)
Label(frame, image = secondbox, bg="#42392F").place(x = 600, y = 40)
Label(frame, image = secondbox, bg="#42392F").place(x = 720, y = 40)
Label(frame, image = secondbox, bg="#42392F").place(x = 840, y = 40)
Label(frame, image = secondbox, bg="#42392F").place(x = 960, y = 40)

# 11. Clock
clock = Label(root, font = ("Calibri", 30, 'bold'), fg = "#FFFFFF", bg = "#42392F")
clock.place(x = 1080, y = 450)

# 11.1 Timezones
timezone = Label(root, font = ("Calibri", 20), fg = "#FFFFFF", bg = "#42392F")
timezone.place(x = 1080, y = 500)

# 11.2 Coordinates
long_lat = Label(root, font = ("Calibri", 15), fg = "#FFFFFF", bg = "#42392F")
long_lat.place(x = 1080, y = 540)

# 12. Display thpwd results
t = Label(root, font = ("Calibri", 12), fg = "#FFFFFF", bg = "#42392F")
t.place(x = 160, y = 150)

# h = humidity
h = Label(root, font = ("Calibri", 12), fg = "#FFFFFF", bg = "#42392F")
h.place(x = 160, y = 170)

# p = pressure
p = Label(root, font = ("Calibri", 12), fg = "#FFFFFF", bg = "#42392F")
p.place(x = 160, y = 190)

# w = wind
w = Label(root, font = ("Calibri", 12), fg = "#FFFFFF", bg = "#42392F")
w.place(x = 160, y = 210)

# d = description
d = Label(root, font = ("Calibri", 12), fg = "#FFFFFF", bg = "#42392F")
d.place(x = 80, y = 250)

# 12. Weather forecast
# cell 1
firstframe = Frame(root,width = 284, height = 132, bg = "#272727")
firstframe.place(x = 50, y = 470)

present = Label(firstframe, font = ("Calibri", 30),  bg = "#272727", fg = "#ffffff")
present.place(x = 45, y = 0)

firstimage = Label(firstframe, bg = "#272727")
firstimage.place(x = 1, y = 10)

presenttemp = Label(firstframe, bg = "#272727", fg = "#ffffff")
presenttemp.place(x = 100, y = 50)

# cell 2
secondframe = Frame(root,width = 80, height = 132, bg = "#272727")
secondframe.place(x = 372, y = 470)

day1 = Label(secondframe, font = ("Calibri", 10),  bg = "#272727", fg = "#ffffff")
day1.place(x = 10, y = 0)

secondimage = Label(secondframe, bg = "#272727")
secondimage.place(x = 1, y = 10)

day1temp = Label(secondframe, bg = "#272727", fg = "#ffffff")
day1temp.place(x = 2, y = 100)

# cell 3
thirdframe = Frame(root,width = 80, height = 132, bg = "#272727")
thirdframe.place(x = 492, y = 470)

day2 = Label(thirdframe, font = ("Calibri", 10),  bg = "#272727", fg = "#ffffff")
day2.place(x = 10, y = 0)

thirdimage = Label(thirdframe, bg = "#272727")
thirdimage.place(x = 1, y = 10)

day2temp = Label(thirdframe, bg = "#272727", fg = "#ffffff")
day2temp.place(x = 2, y = 100)

# cell 4
fourthframe = Frame(root,width = 80, height = 132, bg = "#272727")
fourthframe.place(x = 612, y = 470)

day3 = Label(fourthframe, font = ("Calibri", 10),  bg = "#272727", fg = "#ffffff")
day3.place(x = 10, y = 0)

fourthimage = Label(fourthframe, bg = "#272727")
fourthimage.place(x = 1, y = 10)

day3temp = Label(fourthframe, bg = "#272727", fg = "#ffffff")
day3temp.place(x = 2, y = 100)

# cell 5
fifthframe = Frame(root,width = 80, height = 132, bg = "#272727")
fifthframe.place(x = 732, y = 470)

day4 = Label(fifthframe, font = ("Calibri", 10),  bg = "#272727", fg = "#ffffff")
day4.place(x = 10, y = 0)

fifthimage = Label(fifthframe, bg = "#272727")
fifthimage.place(x = 1, y = 10)

day4temp = Label(fifthframe, bg = "#272727", fg = "#ffffff")
day4temp.place(x = 2, y = 100)

# cell 6
sixthframe = Frame(root,width = 80, height = 132, bg = "#272727")
sixthframe.place(x = 852, y = 470)

day5 = Label(sixthframe, font = ("Calibri", 10),  bg = "#272727", fg = "#ffffff")
day5.place(x = 10, y = 0)

sixthimage = Label(sixthframe, bg = "#272727")
sixthimage.place(x = 1, y = 10)

day5temp = Label(sixthframe, bg = "#272727", fg = "#ffffff")
day5temp.place(x = 2, y = 100)

# cell 7
seventhframe = Frame(root,width = 80, height = 132, bg = "#272727")
seventhframe.place(x = 972, y = 470)

day6 = Label(seventhframe, font = ("Calibri", 10),  bg = "#272727", fg = "#ffffff")
day6.place(x = 12, y = 0)

seventhimage = Label(seventhframe, bg = "#272727")
seventhimage.place(x = 1, y = 10)

day6temp = Label(seventhframe, bg = "#272727", fg = "#ffffff")
day6temp.place(x = 2, y = 100)

root.mainloop()