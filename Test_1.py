import math

mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 107.25
}

data = mobile_data['data']
exchange_rate = mobile_data['exchnage_rate']

for k in data:
    mobile_model = k['name']
    made_in_country = k['made']
    price_in_usd = k['price'].split()[0]
    price_in_bdt = math.ceil(float(price_in_usd) * exchange_rate)
    print(
        f'{mobile_model} is made in {made_in_country}. The price is {price_in_usd} USD which is almost equal to {price_in_bdt} BDT ')
