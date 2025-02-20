import handle_json
import statistics
import random

"""
This module contains ONLY READ commands for 
a JSON file containing nested dictionaries.

Constant preloads nested dictionaries with 
the movie information in the database.
Every function that modifies this global variable
will update the database too.
"""
MOVIE_DATA = handle_json.load_json()


def _print_best_worst_movies(movies, extremes):
    """
    A utility command for the show_stats command.
    Receives a list with the title and rating of the
    best/worst rated movies and formats a string.
    Prints a string.
    """
    if len(movies) == 1:
        print(f"{extremes} movie: {movies[0][1]}, {movies[0][0]}")
    else:
        output_string = f"{extremes} movies: "
        for rating, title in movies:
            output_string += f"{title}, {rating}, "
        print(output_string[:-2])


def _get_best_worst_ratings(rated_movies, highest):
    """
    A utility command for the show_stats command.
    From a list of tuples containing ratings and titles,
    finds the tuples best/worst ratings and returns them
    in a new list.
    """
    extremes_rate = rated_movies[0][0]
    extremes_rate_movies = [rated_movies[0]]

    for rating, title in rated_movies[1:]:
        if highest:
            if rating > extremes_rate:
                extremes_rate = rating
                extremes_rate_movies = [(rating, title)]
            elif rating == extremes_rate:
                if (rating, title) not in extremes_rate_movies:
                    extremes_rate_movies.append((rating, title))
        else:
            if rating < extremes_rate:
                extremes_rate = rating
                extremes_rate_movies = [(rating, title)]
            elif rating == extremes_rate:
                if (rating, title) not in extremes_rate_movies:
                    extremes_rate_movies.append((rating, title))
    return extremes_rate_movies


def _print_movie_data(movies):
    """
    A utility command to print movie data.
    Receives a list of tuples (title, year, rating).
    Prints a string with the info of each tuple.
    """
    for movie in movies:
        title, year, rating = movie
        print(f"{title} ({year}): {rating}")


def _get_title_year_rating():
    """
    A utility command for extracting all the titles along
    with the year and rating of each movie in the database.
    Returns a list with tuples (title, year, rating).
    """
    movies = []
    for movie_title, movie_attributes in MOVIE_DATA.items():
        movie_data = (movie_title, movie_attributes['year'],
                      movie_attributes['rating'])
        movies.append(movie_data)
    return movies


def _get_rating_title():
    """
    A utility command for extracting all the titles and ratings
    from the movie database.
    Returns a list with tuples (rating, title).
    """
    rating_movies = []
    for movie_title, movie_attributes in MOVIE_DATA.items():
        rating_movies.append((movie_attributes['rating'],
                              movie_title))
    return rating_movies


def show_stats(): # Menu command 5
    """
    Calculates and print statistics about the movies in
    the database: average rating, median rating, titles
    with the highest and lowest rating.

    Informs the user when there are no stats to show
    Makes a list with all the ratings in the database
    Prints the average and median averages in the database
    Makes a list of tuples with movie ratings and titles
    Sorts the list of tuples from lowest to highest rating
    Prints the movie(s) with the highest rating
    Prints the movie(s) with the lowest rating
    """
    if len(MOVIE_DATA) < 1:
        print("Currently there are no movies in the database.")
        return

    ratings = []
    for movie in MOVIE_DATA.values():
        ratings.append(movie['rating'])

    # movie_phase1 bonus3, round floats
    average_rating = round(statistics.mean(sorted(ratings)), 2)
    print(f"\nAverage rating: {average_rating}")
    median_rating = round(statistics.median(sorted(ratings)), 2)
    print(f"Median rating: {median_rating}")

    rating_movies = _get_rating_title()
    sorted_ratings_title = sorted(rating_movies,
                                  key=lambda rating: rating[0])

    best_movies = _get_best_worst_ratings(sorted_ratings_title,
                                         highest=True)
    _print_best_worst_movies(best_movies, "Best")

    worst_movies = _get_best_worst_ratings(sorted_ratings_title,
                                          highest=False)
    _print_best_worst_movies(worst_movies, "Worst")


def random_movie(): # Menu command 6
    """
    Prints the title and rating of a random movie
    from the database.
    """
    rating_movies = _get_rating_title()
    _random_movie = random.choice(rating_movies)
    print(f"Your movie for tonight: {_random_movie[1]}, "
          f"it's rated {_random_movie[0]}")


def search_movie(): # Menu command 7
    """
    Asks the user to enter a part of a movie name,
    and then searches all the movies in the database.
    Prints all the movies that matched the user’s query,
    along with the rating. If there is no match it will
    print a message informing the user.
    """
    rating_movies = _get_rating_title()
    search_term = input("Enter part of movie name: ").lower()
    match_found = False

    for rating, title in rating_movies:
        if search_term in title.lower():
            print(f"{title}, {rating}")
            match_found = True

    if not match_found:
        print("Movie matching search term not found")


def list_movies(): # menu command 1
    """
    1. Prints a string indicating how many movies are stored
    in the database (how many dicts are in the dict).
    2. Parses the info from MOVIE_DATA,
    serializes it into a string, and prints it.
    """

    print(f"{len(MOVIE_DATA)} movie(s) in total")

    movies = _get_title_year_rating()

    _print_movie_data(movies)


def sort_by_rating(): # menu command 8
    """
    Fetches and sorts movies sorted by descending rating.
    Prints all the movies and their ratings, in descending
    order by the rating.
    """
    movies = _get_title_year_rating()

    movies_sorted_desc_rating = sorted(movies,
                            key= lambda movies: movies[2],
                            reverse=True)

    _print_movie_data(movies_sorted_desc_rating)


def sort_by_year():
    """
    Fetches and sorts movies by release year.
    Asks user to choose the sorting order.
    Prints all the movies and their ratings, in descending
    or ascending order (most recent or oldest) by year.
    """
    movies = _get_title_year_rating()

    sorted_latest_first = True
    if "n" in input("Do you want the latest movies first? "
                    "(Y/N): ").lower():
        sorted_latest_first = False

    movies_sorted_year = sorted(movies,
                                key= lambda movies: movies[1],
                                reverse=sorted_latest_first)

    _print_movie_data(movies_sorted_year)


def filter_movies():
    """
    Filters data from the database.

    Asks user for filtering options: minimum rating,
    start year, end year. If left blank, changes
    variable to None. Handles ValueError.
    Filtering criteria set to None is ignored.
    Matching movies are appended to a list as tuples
    containing title, year and rating.
    Returns a list with tuples, or prints a message
    indicating no matches were found (list is empty).
    """
    try:
        min_rating_str = input("Enter minimum rating "
                       "(leave blank for no minimum rating): ")
        if min_rating_str:  # if it isn't empty
            min_rating = float(min_rating_str) # convert to float
        else:
            min_rating = None # otherwise set to None

        start_year_str = input("Enter start year "
                       "(leave blank for no start year): ")
        if start_year_str:
            start_year = int(start_year_str)
        else:
            start_year = None

        end_year_str = input("Enter end year "
                     "(leave blank for no end year): ")
        if end_year_str:
            end_year = int(end_year_str)
        else:
            end_year = None
    except ValueError("Please enter valid rating and/or year"):
        return

    filtered_movies = []
    for movie_title, movie_attributes in MOVIE_DATA.items():
        year = movie_attributes.get('year')
        rating = movie_attributes.get('rating')

        if min_rating is None or rating >= min_rating:
            if start_year is None or year >= start_year:
                if end_year is None or year <= end_year:
                    filtered_movies.append((movie_title,
                                        year, rating))

    if filtered_movies:
        print("Filtered Movies: ")
        _print_movie_data(filtered_movies)
    else:
        print("No matches found")
