import requests
s_city = "Moscow,RU"
city_id = 0
appid = "a168022fb51dd4bc2f1c60c27c5fc556"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Прогноз погоды на неделю:")
    for i in data['list']:
        print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'], i['visibility'],  i['wind']['speed'])
except Exception as e:
    print("Exception (forecast):", e)
    pass