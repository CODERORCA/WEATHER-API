# WEATHER-API

This is a little project trying out to fetch data in form of an API to project a weather forecast using Python tkinter package. This API works only on Windows!

With this API you can:

- Type a location of your choice into the search bar
- Get current time, the timezone and the exact coordinates of the specified location
- Get current weather information such as Temperature, Humidity, Pressure, Wind Speed and a Description
- Get a weather forecast for the next 6 days
- Retrieve data about the average temperature during day and nighttime

! Before you open the API there are important information you should be aquainted with !

// Table of content
1. Install pacakages
2. Install the API
3. Modify the script
4. API Key
5. Launching the script

// 1. Install packages

If you haven't done that in the past I recommend to check if you have additional packages installed.
This API requires you to have these packages installed:

- geopy
- datetime
- timezonefinder
- requests
- pytz
- pillow

If you don't then don't worry. All you have to do is to Open CMD (Command Prompt) and type in

pip install (package name)

and windows should do the rest

// 2. Install the API

Download the files from my repository and extract them on your Desktop. Once you have done that you should see
weather_api_1.1.0 on your desktop. Check if the following files are located inside that folder:

icon (Folder)

images (Folder)

license (.txt file)

README (.txt file)

weather.py (Python script)


// 3. Modify the API

In order to be able to launch the API you have to check the directory file paths inside the script.
Use a file editor of your choice (VSCode, IntelliJ, Eclipse...)
Following lines need to have the directory changed if your copy of the script doesn't work
22, 26, 31, 36, 43, 101, 115, 131, 147, 163, 179, 195, 247, 256 and 257
You will see something like this: "Desktop/weather_api_v1.1.0/images/logo.png"

Since the weather_api folder is on the desktop it may or may not work on first try. In this case modify the filepath accordingly.
You may need to write something like this: C:/Users/"pc name"/ in front of Desktop/weather_api_v1.1.0/images/logo.png. 

Once done that you can launch it


// 4. API Key

Line 78 contains the following syntax:

api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid={API Key}"
This API is fetching data from www.openweathermap.org for which if you want to make use of the API key, you must register and subscribe
Fortunately, the subscription of the One Call 3.0 feature is for free.

Please visit www.openweathermap.org and follow the Guide there.
You have to create an API Key on this Website and then replace

{API Key} 

with the numeric API key it got generated on your account.

// 5. Launching the script

You should be able to launch it without the need for an IDLE or any Editor. In case of trouble please feel free to contribute, request a pull or contact me via E-Mail coderorca@outlook.com

This project was done on a free basis and for educational purposes. Please reade the license.txt file for more information about handling and distributing the files.
