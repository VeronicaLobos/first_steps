import json
import os


def load_json(filepath="movies.json")
    """
    Loads a json file containing data about movies.
    
    Checks if the file exists. Ff it doesn't, creates
    and populates a new json file with example data.
    
    Handles errors by returning an empty dictionary.
    
    Returns a dictionary where keys = movie titles, 
    values = dictionaries with movie attributes like
    rating and release year).
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
                json.dump(movie_example, handle)

        with open(file=file_path, mode="r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print("File not found.")
        return {}
    except json.JSONDecodeError:
        print("JSON file is corrupted")
        return {}
