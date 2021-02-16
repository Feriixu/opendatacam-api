import requests as re


class Webcam:
    def __init__(self, base_url):
        self.base_url = base_url

    # Webcam methods
    def get_resolution(self):
        return re.get(f'{self.base_url}/webcam/resolution').json()

    def get_stream_url(self):
        return f'{self.base_url}/webcam/stream'
