import requests
from rest_framework import status
from django.conf import settings


def convert_currencies(rub_price):
    """Реализовать получение курса валют от сервиса currencyapi.com/ для вывода суммы машины или мотоцикла в долларах
    при условии, что изначально все суммы заводились в рублях."""
    usd_price = 0
    usd_rate = 0
    response = requests.get(f'{settings.CUR_API_URL}v3/latest?apikey={settings.CUR_API_KEY}&currencies=RUB')
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price * usd_rate / 10000
    return usd_price


def convert_eur(rub_price):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=RUB&amount={rub_price}"
    payload = {}
    headers = {"apikey": settings.CUR_KEY_APILAYER}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    return result['result']
