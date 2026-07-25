import json


class Config:
    def __init__(self, config_file="config/settings.json"):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.config_file} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.config_file}.")
            return {}

    def get(self, key, default=None):
        return self.settings.get(key, default)
