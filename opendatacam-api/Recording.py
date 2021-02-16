import requests as re


class Recording:
    def __init__(self, base_url):
        self.base_url = base_url

    # Recordings Methods
    def get_counter_data(self, id: str):
        return re.get(f'{self.base_url}/recording/{id}/counter').json()

    def get_counter_data_csv(self, id: str):
        return re.get(f'{self.base_url}/recording/{id}/counter/csv').content

    def delete(self, id: str):
        re.delete(f'{self.base_url}/recording/{id}')

    def get_details(self, id: str):
        return re.get(f'{self.base_url}/recording/{id}').json()

    def start(self):
        re.get(f'{self.base_url}/recording/start')

    def stop(self):
        re.get(f'{self.base_url}/recording/stop')

    def get_tracker_data(self, id: str):
        re.get(f'{self.base_url}/recording/{id}/tracker').json()

    def list(self, offset: int = None, limit: int = None):
        params = {
            "offset": offset,
            "limit": limit
        }
        return re.get(f'{self.base_url}/recordings', params=params).json()
