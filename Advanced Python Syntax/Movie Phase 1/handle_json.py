import json
import os

FILE_NAME = "movies.json"

"""This module contains functions to READ and WRITE the 
movie data base (static JSON file). These are called by
the functions in the
movie_storage module.

This program uses nested dictionaries and persistent data.
The outer dictionary uses movie titles as keys, and each key
maps to another dictionary containing movie attributes
(year, rating).
"""

def update_json(updated_movie_data):
    """
    Writes the dictionary updated_movie_data to the json file.
    """
    with open(file=FILE_NAME, mode='w',
              encoding="utf-8") as handle:
        json.dump(updated_movie_data, handle, indent=4)


def load_json(filepath=FILE_NAME):
    """
    Loads a json file containing data about movies.
    
    Checks if the file exists. If it doesn't, creates
    and populates a new json file with example data.

    Handles errors by returning an empty dictionary.
    
    Returns a dictionary where keys = movie titles, 
    values = dictionaries with movie attributes like
    rating and release year.

    Handles errors for missing or corrupted JSON file.
    """
    movie_dict_example = {
        "Titanic": {
            "rating": 9,
            "year": 1999
        }
    }

    try:
        if not os.path.exists(filepath):
            with open(file=filepath, mode='w',
                      encoding="utf-8") as handle:
                json.dump(movie_dict_example, handle, indent=4)

        with open(file=filepath, mode="r",
                  encoding="utf-8") as handle:
            return json.load(handle)

    except FileNotFoundError:
        print(f"{filepath} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"{filepath} is corrupted")
        return {}

MOVIE_DATA = load_json()
