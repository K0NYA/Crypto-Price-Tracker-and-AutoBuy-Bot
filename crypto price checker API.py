import requests

url = "https://api.binance.com/api/v3/ticker/price"

querystring = {"symbol":"BTCUSDT"}

response = requests.request("GET", url, params=querystring)

print(response.text)

def check_price_change():
    url = "https://api.binance.com/api/v3/ticker/price"
    querystring = {"symbol":"BTCUSDT"}
    response = requests.request("GET", url, params=querystring)
    current_price = float(response.json()['price'])
    historical_price = get_historical_price() # a function that retrieves historical price
    if current_price > historical_price:
        print("Price of BTC in USDT has increased from {} to {}".format(historical_price, current_price))
    elif current_price < historical_price:
        print("Price of BTC in USDT has decreased from {} to {}".format(historical_price, current_price))
    else:
        print("Price of BTC in USDT has not changed")
