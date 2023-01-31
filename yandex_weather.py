import requests
from Key import Yandex_Weather_TOKEN



url = 'https://api.weather.yandex.ru/v2/forecast'
coords = 55.755864, 37.617698



response = requests.get(
    url,
    params={
        'lat': coords[0],
        'lon': coords[1],
        'lang': 'ru_RU'
    },
    headers={'X-Yandex-API-Key': Yandex_Weather_TOKEN}
)

print(response.status_code)
weather = response.json()
print(weather)

fact = weather['fact']
print(fact)