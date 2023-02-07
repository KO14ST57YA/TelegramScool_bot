import requests
from Key import Yandex_Weather_TOKEN


def get_weather():
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

    # TODO Обработать ситуацию с ошибкой
    weather = response.json()

    # for i in weather:
    #     print(i, weather[i])
    city_name = weather['geo_object']['locality']['name']
    weather_fact = weather['fact']

    conditions = {
        'clear': 'ясно',
        'partly-cloudy': 'partly-cloudy',
        'cloudy': 'облачно с прояснениями',
        'overcast': 'пасмурно',
        'drizzle': 'морось',
        'light - rain': 'небольшой дождь',
        'rain': 'дождь',
        'moderate-rain' : 'умеренно сильный дождь',
        'heavy - rain': 'сильный дождь',
        'continuous - heavy - rain' : 'длительный сильный дождь',
        'showers': 'ливень',
        'wet-snow': 'дождь со снегом',
        'light-snow': 'небольшой снег',
        'snow': 'снег',
        'snow-showers': 'снегопад',
        'hail': 'град',
        'thunderstorm': 'гроза',
        'thunderstorm-with-rain': 'дождь с грозой',
        'thunderstorm-with-hail': 'гроза с градом'
    }


    to_user = {
        'status_code': response.status_code,
        'Город': city_name,
        'Температура': weather_fact['temp'],
        'Ощущается, как': weather_fact['feels_like'],
        'Состояние': conditions[weather_fact['condition']],
    }
    return to_user


# for key in weather_fact:
#     print(key, weather_fact[key])
