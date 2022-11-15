import requests
from config import open_weather_token
from pprint import pp
import datetime

def get_weather(city, open_weather_token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru")
        data = r.json()
        #pp(data)
        city = data["name"]
        des = data["weather"][0]["description"]
        cur_weather = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        print(f"Название города: {city}\n"
              f"Текущая погода: {des}\n"
              f"Температура воздуха: {cur_weather}°C\n"
              f"Атмосферное давление: {pressure} мм.рт.ст.\n"
              f"Влажность воздуха: {humidity}%\n"
              f"Скорость ветра: {wind} м/с\n"
              f"Код страны: {country}\n"
              f"Восход: {sunrise}")
    except Exception as ex:
        print(ex)
        print("Проверьте название города")



def main():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)
if __name__ == "__main__":
    main()