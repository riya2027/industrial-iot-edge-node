import json


def load_thresholds():

    with open("config/thresholds.json", "r") as file:
        return json.load(file)