import requests

api_key='0782804abc9da2ef78460cc53b5a1e88'

user_input=input('Enter the city: ')

weather_info=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)
if weather_info.json() ["cod"]=="404":
    print("Couldnt find city.")
else:
    weather=weather_info.json()["weather"][0]["main"]
    temp=round(weather_info.json()["main"]["temp"])
    temp_celsius=round((temp-32) * (5/9),1)

    print(f"The weather of {user_input} is : {weather}")
    print(f"The temperature is :{temp} F / {temp_celsius} C")


