import json
import os

FILE_NAME = "movies.json"

"""This module contains functions for reading and writing the 
movie data base. These are called by the functions in the
movie_storage module.

This program uses nested dictionaries and persistent data.
The outer dictionary uses movie titles as keys, and each key
maps to another dictionary containing movie attributes
(year, rating). 
"""

def update_json(updated_movie_data):
    """
    Loads a json file containing data about movies in
    writing mode.


    (...)
    """
    with open(file=FILE_NAME, mode='w', encoding="utf-8") as handle:
        json.dump(updated_movie_data, handle, indent=4)


def load_json(filepath=FILE_NAME):
    """
    Loads a json file containing data about movies in
    reading mode.
    
    Checks if the file exists. If it doesn't, creates
    and populates a new json file with example data.

    Handles errors by returning an empty dictionary.
    
    Returns a dictionary where keys = movie titles, 
    values = dictionaries with movie attributes like
    rating and release year.
    """
    movie_dict_example = {
        "Titanic": {
            "rating": 9,
            "year": 1999
        }
    }

    try:
        if not os.path.exists(filepath):
            with open(file=filepath, mode='w', encoding="utf-8") as handle:
                json.dump(movie_dict_example, handle, indent=4)

        with open(file=filepath, mode="r", encoding="utf-8") as handle:
            return json.load(handle)

    except FileNotFoundError:
        print(f"{filepath} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"{filepath} is corrupted")
        return {}
