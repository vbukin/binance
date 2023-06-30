import sys

from client import Client
from currency import Currency
from utils import lower_price, FileWriter


def main():
    symbols = ['BTCUSDT', 'MAVTUSD', 'BNBUSDT', 'FLOKITRY', 'RDNTUSDT', 'GALAAUD']
    basic_currency = 'BTCUSDT'

    client = Client()
    cur = Currency(client, symbols)
    response = cur.get()

    status_code = response.status_code
    if status_code != 200:
        print(f'Incorrect response status code: {status_code}\nbody: {response.text}')
        sys.exit(1)

    data = response.json()
    prices = {item['symbol']: item['price'] for item in data}

    writer = FileWriter()
    writer.delete_file()
    writer.write(prices)

    low_price = lower_price(prices, basic_currency)
    if not low_price:
        writer.write(f'Did not find any less currency than {basic_currency}')
    else:
        writer.write(f'Currency less than {basic_currency}: ')
        writer.write(low_price)


if __name__ == '__main__':
    main()
