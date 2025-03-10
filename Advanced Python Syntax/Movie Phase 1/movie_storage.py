import handle_json
from handle_json import MOVIE_DATA

"""
This module contains commands that READ and WRITE
a JSON file.

MOVIE_DATA preloads nested dictionaries
with the movie information in the database.

A utility command, _update_database(), 
"""


def _update_database():
    """
    A utility command for updating the database.
    Overwrites the JSON file with the data stored
    in the constant MOVIE_DATA.
    """
    handle_json.update_json(MOVIE_DATA)


def _check_empty_dict():
    """
    A utility command for checking if there is
    data stored in the dictionary/database, if so
    returns True.
    """
    return len(MOVIE_DATA) == 0


def _movie_exists(movie_title):
    """
    A utility command for checking if a movie is
    already in the database, if so returns True.
    """
    if movie_title in MOVIE_DATA:
        return True
    else:
        return False


def _check_title():
    """
    A utility command for checking correct input
    for a movie's title. Keeps prompting for input.
    Returns a string.
    """
    while True:
        movie_title = input("Enter movie name: ")
        if not movie_title:
            print("Title cannot be empty.")
            continue
        break
    return movie_title


def _check_year():
    """
    A utility command for checking correct input
    for a movie's release year. Keeps prompting for input.
    Returns an integer.
    """
    while True:
        try:
            movie_year = int(input("Enter new movie year: "))
            if (len(str(movie_year))) != 4 or not (
                    1894 <= movie_year <= 2030
            ):
                print("Please enter a valid year with four digits.")
                continue
        except (ValueError, TypeError):
            print("Please enter a valid year with four digits.")
        break
    return movie_year


def _check_rating():
    """
    A utility command for checking correct input
    for a movie's rating. Keeps prompting for input.
    Returns a float, rounds to a single decimal
    """
    while True:
        try:
            # movie_phase1 bonus3, round floats
            movie_rating = round(float(input(
                "Enter new Movie rating: ")), 1)
            if not 0.0 <= movie_rating <= 10.0:
                print("Rating must be a valid number"
                      "between 0.0 and 10.0")
                continue
        except (ValueError, TypeError):
            print("Rating must be a valid number"
                  "between 0.0 and 10.0")
            continue
        break
    return movie_rating

"""
note: list_movies() Menu command 1 moved to module
movie_stats, since it shares utility commands with
another command, sort_by_rating() Menu command 8
"""


def add_movie(): # Menu command 2
    """
    Adds a movie to the movie database.

    Checks if the movie already exists in the database.
    If it doesn't exist, creates a dictionary
    with the new movie data, and updates the database.
    Checks if the movie was successfully added.
    Prints a message informing the user of the resulting
    operation.
    """
    movie_title = _check_title()

    if _movie_exists(movie_title):
        print(f"{movie_title} already exists in database")
    else:
        MOVIE_DATA[movie_title] = {
            "rating": _check_rating(),
            "year": _check_year()
            }

        _update_database()

        if _movie_exists(movie_title):
            print(f"{movie_title} successfully added")
        else:
            print("Something went wrong, movie not added")


def delete_movie(): # Menu command 3
    """
    Deletes a movie from the movie database.

    Checks if there is data to delete, if so
    Checks if the movie exists in the database, if so
    Deletes the movie from the preloaded
    dict of dicts, and updates the json file with it.
    Raises a KeyError if the movie cannot be found
    in the database and thus, the operation cannot be
    performed (still same result).

    Prints a message to inform the user of the operation
    result.
    """
    if _check_empty_dict():
        print("Currently there are no movies in the database")
        return

    movie_title = _check_title()

    try:
        if not _movie_exists(movie_title):
            raise KeyError(f"Movie {movie_title} doesn't exist!")

        del MOVIE_DATA[movie_title]
        _update_database()
        print(f"Movie {movie_title} successfully deleted")
    except KeyError:
        print(f"Movie {movie_title} doesn't exist!")


def update_movie(): # Menu command 4
    """
    Updates a movie rating from the movie database.

    Checks if there is no data to update. Otherwise,
    Modifies the value in the preloaded dict of dicts,
    and then updates the json file with it.
    Raises a KeyError if the movie cannot be found
    in the database and thus, the operation cannot be
    performed (still same result).

    Prints a message to inform the user of the operation
    result.
    """
    if _check_empty_dict():
        print("Currently there are no movies in the database")
        return

    movie_title = _check_title()

    try:
        if not _movie_exists(movie_title):
            print(f"Movie {movie_title} doesn't exist!")
            return
        new_movie_rating = _check_rating()
        MOVIE_DATA[movie_title]["rating"] = new_movie_rating
        _update_database()
        print(f"Movie {movie_title} successfully updated")
    except KeyError:
        print(f"Movie {movie_title} doesn't exist!")
