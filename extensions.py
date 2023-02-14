import requests
import json
from config import keys

class APIExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExeption(f'Введите, пожалуйста, разные валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExeption(f'"{quote}" нет в списке доступных валют')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExeption(f'"{base}" нет в списке доступных валют')
        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'"{amount}" не является целым числом')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base