from typing import Union

from client import Client


class Currency:
    def __init__(self, client: Client, symbols: Union[list, str] = None):
        self.client = client
        self.symbols = symbols
        self.path = '/ticker/price'

    def get(self):
        symbols_path = '' if self.symbols is None else self.get_path()
        return self.client.get(self.path + symbols_path)

    def get_path(self):
        if type(self.symbols) == str:
            path = f'?symbol={self.symbols}'
        else:
            symbols_string = '[' + ','.join([f'"{symbol}"' for symbol in self.symbols]) + ']'
            path = f'?symbols={symbols_string}'
        return path
