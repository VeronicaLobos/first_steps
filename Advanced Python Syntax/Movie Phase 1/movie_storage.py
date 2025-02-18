import handle_json
import re

"""
Preloads into a constant a dictionary of dictionaries that
contains the movies information in the database.
"""
MOVIE_DATA = handle_json.load_json()


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
    Creates a dictionary with the new movie data,
    but first checks if the movie is already in the database,
    and then, checks user input for wrong data types, keeps
    prompting the user for valid input.

    (...)
    """

    """1. Get new movie title"""
    while True:
        new_movie_title = input("Enter new movie name: ").strip(".")
        if not new_movie_title:
            print("Title cannot be empty.")
            continue
        if not isinstance(new_movie_title, str):
            print("Title must be a string.")
            continue
        if new_movie_title in MOVIE_DATA.keys():
            print(f"{new_movie_title} already exists in the database.")
            continue
        break

    """2. Get new movie year"""
    while True:
        try:
            new_movie_year = int(input("Enter new movie year: "))
            if (len(str(new_movie_year))) != 4 or not (
                    1894 <= new_movie_year <= 2030
            ):
                print("Please enter a valid year with four digits.")
                continue
        except (ValueError, TypeError):
            print("Please enter a valid year with four digits.")
        break

    """3. Get new movie rating"""
    while True:
        try:
            new_movie_rating = round(float(input("Enter new Movie rating: ")), 1)
            if (not 0 <= new_movie_rating <= 10 and not \
            re.fullmatch(r"^[0-9]+(\.[0-9]+)?$", new_movie_rating)):
                print("Rating must be a valid number between 0.0 and 10.0")
                continue
        except TypeError:
            print("Rating must be a valid number between 0.0 and 10.0")
        break

    """4. Formats the input into a dictionary and updates MOVIE_DATA"""
    MOVIE_DATA[new_movie_title] = {
        "rating": new_movie_rating,
        "year": new_movie_year
        }

    """5. Updates the data base with the newest version of MOVIE_DATA"""
    handle_json.update_json(MOVIE_DATA)

    """6. Checks if the new movie/dict was added to the database"""
    if new_movie_title in MOVIE_DATA:
        print(f"{new_movie_title} successfully added")
    else:
        print("Something went wrong")


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
    movie_title = input("Enter movie name to delete: ")
    try:
        del MOVIE_DATA[movie_title]
        print(MOVIE_DATA)
        if movie_title not in MOVIE_DATA:
            handle_json.update_json(MOVIE_DATA)
            print(f"Movie {movie_title} successfully deleted")
    except KeyError:
        print(f"Movie {movie_title} doesn't exist!")


def update_movie():
    """
    Updates a movie from the movie database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    pass
  