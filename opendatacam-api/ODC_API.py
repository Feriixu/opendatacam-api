import requests as re
from sseclient import SSEClient
from Helper import Helper
from Recording import Recording
from Counter import Counter
from Webcam import Webcam


class ODC_API:
    def __init__(self, base_url: str):
        self.base_url = base_url.strip('/')

        self.helper = Helper(base_url)
        self.recording = Recording(base_url)
        self.counter = Counter(base_url)
        self.webcam = Webcam(base_url)

    # Opendatacam Methods
    def start(self):
        re.get(f'{self.base_url}/start')

    def get_sse_client(self):
        return SSEClient(f'{self.base_url}/tracker/sse')
