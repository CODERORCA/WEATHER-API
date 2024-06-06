# WEATHER-API
Before you open the API there are important information you should be aquainted with

1. Install the API
2. Modify the script
3. API Key
4. Launching the script


1. In order to use the API please extract the weather_api folder and place it on your desktop
1.1. Open the folder and make sure following folders and files are visible:

Name:       Type:
icon        (Folder)
images      (Folder)
licnese     (.txt file)
README      (.txt file)
weather.py  (Python script)

This is important so the script can read the files

2. Modify the API
In order to be able to launch the API you have to check the directory file paths inside the script.
Use a file editor of your choice (VSCode, IntelliJ, Eclipse...)
Following lines need to have the directory changed if your copy of the script doesn't work
22, 26, 31, 36, 43, 101, 115, 131, 147, 163, 179, 195, 247, 256 and 257
You will see something like this: "Desktop/weather_api/images/logo.png"

Since the weather_api folder is on the desktop it may or may not work on first try. In this case modify the filepath accordingly.
You may need to write something like this: C:/Users/<pc name>/ in front of Desktop/weather_api/images/logo.png. 

Once done that you can launch it

3. API Key
Line 78 contains the following syntax 
api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid={API Key}"
This API is fetching data from www.openweathermap.org for which if you want to make use of the API key, you must register and subscribe
Fortunately, the subscription of the One Call 3.0 feature is for free. Please visit www.openweathermap.org and follow the Guide there.
You have to create an API Key on this Website and then replace

{API Key} 

with the numeric API key it got generated on your account.

5. Launching it
This script sadly comes with a bug which won't allow you to open it without using the Python IDLE.
Please run the script using your favorite Editor (Preferably, VSCode or the Mu Editor but other editors should also work fine)

This API is work in progress and is subject to changes and improvements will be made over time.
