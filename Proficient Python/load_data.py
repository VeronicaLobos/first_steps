import json

def load_data():
  """ Loads a JSON file """
  with open("ships_data.json", "r") as handle:
    return json.load(handle)
