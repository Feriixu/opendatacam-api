import requests as re


class Counter:
    def __init__(self, base_url):
        self.base_url = base_url

    # Counter Methods
    def counter_get_areas(self):
        return re.get(f'{self.baseUrl}/counter/areas').json()


