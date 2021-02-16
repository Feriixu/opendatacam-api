import requests as re


class Helper:
    def __init__(self, base_url):
        self.base_url = base_url

    # Helper Methods
    def get_config(self):
        return re.get(f'{self.base_url}/config').json()

    def get_console(self):
        return re.get(f'{self.base_url}/console').content

    def get_ui_settings(self):
        return re.get(f'{self.base_url}/ui').json()

    def set_ui_settings(self, counterEnabled, pathfinderEnabled):
        data = {
            "counterEnabled": counterEnabled,
            "pathfinderEnabled": pathfinderEnabled
        }
        re.post(f'{self.base_url}/ui', json=data)

    def get_status(self):
        return re.get(f'{self.base_url}/status').json()
