import requests
s_city = "Moscow,RU"
city_id = 0
appid = "a168022fb51dd4bc2f1c60c27c5fc556"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Город:", s_city)
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура", data['main']['temp_max'])
    print("Видимость:", data['visibility'])
    print("Скорость ветра:", data['wind']['speed'])
except Exception as e:
    print("Exception (forecast):", e)
    pass