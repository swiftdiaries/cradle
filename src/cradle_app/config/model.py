from pathlib import Path

import yaml


class Config:
    name = ""
    uri = ""

    def __init__(self, path):
        with open(path, "r") as config_file:
            try:
                model_config = yaml.safe_load(config_file)
                self.name = model_config["name"]
                self.uri = model_config["uri"]
            except yaml.YAMLError as exc:
                print(exc)

    def show(self):
        print("Model config:\n")
        print(f"Model Name: {self.name}")
        print(f"Model URI: {self.uri}")
