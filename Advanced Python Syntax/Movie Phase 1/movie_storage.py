import load_json

"""
Loads into a constant a dictionary of dictionaries that
contains the movies information in the database.
"""
MOVIE_DATA = load_json.load_json()


def list_movies():
    """
    1. Prints a string indicating how many movies are stored
    in the database (how many dicts are in the dict).
    2. Parses the info from MOVIE_DATA,
    serializes it into a string, and prints it.
    """

    print(f"{len(MOVIE_DATA)} movie(s) in total")

    for movie_title, movie_attributes in MOVIE_DATA.items():
        movie_release_year = movie_attributes.get("year"): int
        movie_rating = movie_attributes.get("rating"): float
        print(f"{movie_title} ({movie_release_year}): {movie_rating}")


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    pass


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    pass


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    pass
  