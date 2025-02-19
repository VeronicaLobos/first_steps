import handle_json
import statistics

"""
Preloads into a constant a dictionary of dictionaries
with the movie information in the database.
"""
MOVIE_DATA = handle_json.load_json()


def _print_bestworst(movies, extremes):
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


def _get_bestworse_ratings(rated_movies, highest):
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


def show_stats():
    """
    Print statistics about the movies in the database:
    average rating, median rating, titles with the highest
    and lowest rating.
    Only reads, doesn't modify the database.
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
    rating_movies = []
    for movie_title, movie_attributes in MOVIE_DATA.items():
        rating_movies.append((movie_attributes['rating'],
                              movie_title))

    #   4. Sorts the list of tuples from lowest to highest rating
    sorted_ratings_title = sorted(rating_movies,
                                  key=lambda rating: rating[0])

    #   5. Prints the movie(s) with highest rating
    best_movies = _get_bestworse_ratings(sorted_ratings_title,
                                         highest=True)
    _print_bestworst(best_movies, "Best")

    #   4. Prints the movie(s) with lowest rating
    worst_movies = _get_bestworse_ratings(sorted_ratings_title,
                                          highest=False)
    _print_bestworst(worst_movies, "Worst")
