# exchange_rate_api.py
import requests

EXCHANGE_TOKEN = "c9d87aef-825c-4b5a-b0de-316a1133aee4"
def obtener_usd_clp_general():
    url = f"https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=CLP&apikey={EXCHANGE_TOKEN}"
    resp = requests.get(url)
    data = resp.json()
    return data["rates"]["CLP"]
