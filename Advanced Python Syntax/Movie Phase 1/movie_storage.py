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
        movie_release_year = movie_attributes.get("year")
        movie_rating = movie_attributes.get("rating")
        print(f"{movie_title} ({movie_release_year}): {movie_rating}")


def add_movie():
    """
    Adds a movie to the movies database.
    Creates a dictionary with the new movie data,
    but first checks if the movie is already in the database
    and checks user input for wrong data types, keeps prompting
    the user for valid input.

    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """

    """Get new movie title"""
    while True:
        new_movie_title = input("Enter new movie name: ").strip(".")
        if not new_movie_title:
            print("Title cannot be empty.")
            continue
        if not isinstance(new_movie_title, str):
            print("Title must be a string.")
            continue
        if new_movie_title in MOVIE_DATA.keys():
            print(f"{new_movie_title} already exists in database.")
            continue
        break

    """Get new movie year"""
    while True:
        try:
            new_movie_release_year = int(input("Enter new movie year: "))
            if len(str(new_movie_release_year)) != 4:
                print("Please enter a valid year with four digits.")
                continue
        except (ValueError, TypeError):
            print("Please enter a valid year with four digits.")
        break

    """Get new movie rating"""
    while True:
        try:
            new_movie_rating = round(float(input("Enter new Movie rating: ")))
            if not 0 <= new_movie_rating <= 10:
                print("Rating must be a valid number between 0.0 and 10.0")
                continue
        except TypeError:
            print("Rating must be a valid number between 0.0 and 10.0")
        break

    """Formats the input into a dictionary and updates MOVIE_DATA"""
    MOVIE_DATA[new_movie_title] = {
        "rating": new_movie_rating,
        "year": new_movie_release_year
        }

    """Updates the data base with the newest version of MOVIE_DATA"""
    load_json.update_json(MOVIE_DATA)

    """Checks if the new movie/dict was added to the database"""
    if new_movie_title in MOVIE_DATA:
        print(f"{new_movie_title} successfully added")
    else:
        print("Something went wrong")


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
  