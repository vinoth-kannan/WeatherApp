import requests
import json

API_KEY="634bd36938f268329d34a8223e89ff73"
base_url="https://api.openweathermap.org/data/2.5/weather?q="

print("\n------- Weather App -------")
city =input("Enter a city name : ")

complete_url=base_url+city+"&appid="+API_KEY
API_Response=requests.get(complete_url)
json_Response=API_Response.json()


temp="{:.2f}".format((json_Response["main"]["temp"])-273.15)
max_temp="{:.2f}".format((json_Response["main"]["temp_max"])-273.15)
min_temp="{:.2f}".format((json_Response["main"]["temp_min"])-273.15)
humid=json_Response["main"]["humidity"]
wind_speed=json_Response["wind"]["speed"]
wind_dir=json_Response["wind"]["deg"]
cloudiness=json_Response["clouds"]["all"]


print("\nWeather conditions in ",city," : \n")
print(f"Temperature : {temp} \u2070C")
print(f"Maximum Temperature : {max_temp}\u2070C")
print(f"Minimum Temperature : {min_temp}\u2070C")
print(f"Humidity : {humid}%")
print(f"Wind Speed : {wind_speed} m/s")
print(f"Wind Direction : {wind_dir} deg due North")
print(f"Cloudiness : {cloudiness}%\n")
print("---------------------")