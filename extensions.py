import requests
import json
from config import keys


class  APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise  APIException(f'Невозможно перевести одинаковые валюты {quote}!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise  APIException(f'Невозможно обработать валюту {quote}!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise  APIException(f'Невозможно обработать валюту {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise  APIException(f'Не удалось обработать количество {amount}!')

        r=requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base =round(json.loads(r.content)[keys[base]] * amount, 3)

        return total_base