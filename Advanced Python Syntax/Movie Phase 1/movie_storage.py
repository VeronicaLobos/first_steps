import handle_json
import re

"""
Preloads into a constant a dictionary of dictionaries
with the movie information in the database.
"""
MOVIE_DATA = handle_json.load_json()


def _update_database():
    """
    A utility command for updating the database
    """
    handle_json.update_json(MOVIE_DATA)


def _check_empty_dict():
    if len(MOVIE_DATA) == 0:
        return True
    else:
        return False


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
    A utility command for checking the title
    Keeps prompting for input
    Returns a string
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
    A utility command for checking the year
    Keeps prompting for input
    Returns an integer
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
    A utility command for checking the rating
    Keeps prompting for input
    Returns a float, rounds to a single decimal
    """
    while True:
        try:
            movie_rating = round(float(input("Enter new Movie rating: ")), 1)
            if not 0.0 <= movie_rating <= 10.0:
                print("Rating must be a valid number between 0.0 and 10.0")
                continue
        except (ValueError, TypeError):
            print("Rating must be a valid number between 0.0 and 10.0")
            continue
        break
    return movie_rating


def list_movies():
    """
    1. Prints a string indicating how many movies are stored
    in the database (how many dicts are in the dict).
    2. Parses the info from MOVIE_DATA,
    serializes it into a string, and prints it.
    """

    print(f"{len(MOVIE_DATA)} movie(s) in total")

    for movie_title, movie_attributes in MOVIE_DATA.items():
        movie_release_year = movie_attributes.get("year")
        movie_rating = movie_attributes.get("rating")
        print(f"{movie_title} ({movie_release_year}): {movie_rating}")


def add_movie():
    """
    Adds a movie to the movie database.
    CHeck if the movie already exists.
    Creates a dictionary with the new movie data.
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


def delete_movie():
    """
    Deletes a movie from the movie database.
    Deletes the movie from the preloaded dict of dicts,
    and updates the json file with it.

    Prints a message to inform the user of the operation
    result. Raises a KeyError if the movie cannot be found
    in the database and thus, the operation cannot be
    performed (still same result).
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


def update_movie():
    """
    Updates a movie rating from the movie database.

    Modifies the value in the preloaded dict of dicts,
    and then updates the json file with it.
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