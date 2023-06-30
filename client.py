import sys

import requests

from config import URL


class Client:
    def get(self, path_url) -> requests.Response:
        url = URL + path_url

        try:
            re = requests.get(url=url)
        except requests.exceptions.ConnectionError as e:
            print('Connection error', str(e))
            sys.exit(1)

        return re
