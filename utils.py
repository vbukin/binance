import os
from typing import Union


class FileWriter:
    def __init__(self, path: str = 'result.txt'):
        self.path = path

    def write(self, prices: Union[dict, str, list]):
        with open(self.path, 'a', encoding='utf-8') as file:
            if isinstance(prices, dict):
                for symbol, price in prices.items():
                    file.write(f"{symbol}: {price}\n")
            elif isinstance(prices, str):
                file.write(prices)
            elif isinstance(prices, list):
                file.write(', '.join(prices) + '\n')

    def delete_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)
            print(f"File '{self.path}' deleted.")
        else:
            print(f"File '{self.path}' does not exist.")


def lower_price(prices: dict, higher_ticket: str) -> list:
    higher_price = prices[higher_ticket]
    return [symbol for symbol, price in prices.items() if price < higher_price]
