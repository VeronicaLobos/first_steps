import handle_json
import statistics
import random

"""
This module contains ONLY READ commands for 
a JSON file containing nested dictionaries.

Constant preloads nested dictionaries with 
the movie information in the database.
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
    Print statistics about the movies in the database:
    average rating, median rating, titles with the highest
    and lowest rating.
    """

    #   0. Informs the user when there are no stats to show
    if len(MOVIE_DATA) < 1:
        print("Currently there are no movies in the database.")
        return

    #   1. Makes a list with all the ratings in the database
    ratings = []
    for movie in MOVIE_DATA.values():
        ratings.append(movie['rating'])

    #   2. Prints the average and median averages in the database
    average_rating = statistics.mean(sorted(ratings))
    print(f"\nAverage rating: {average_rating}")
    median_rating = statistics.median(sorted(ratings))
    print(f"Median rating: {median_rating}")

    #   3. Makes a list of tuples with movie ratings and titles
    rating_movies = _get_rating_title()

    #   4. Sorts the list of tuples from lowest to highest rating
    sorted_ratings_title = sorted(rating_movies,
                                  key=lambda rating: rating[0])

    #   5. Prints the movie(s) with highest rating
    best_movies = _get_best_worst_ratings(sorted_ratings_title,
                                         highest=True)
    _print_best_worst_movies(best_movies, "Best")

    #   4. Prints the movie(s) with lowest rating
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