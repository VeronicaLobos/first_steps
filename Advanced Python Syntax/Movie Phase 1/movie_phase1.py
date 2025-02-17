import sys
import movie_storage


def command_dispatcher(user_input):
    """
    Returns a value from a dictionary pairing the
    menu options with the functions available to
    the user in the CLI
    """
    commands = {
        0: exit,  # tested
        1: movie_storage.list_movies, # tested
        2: movie_storage.add_movie, # tested
        3: movie_storage.delete_movie, # tested
        4: movie_storage.update_movie, # tested
        5: "Stats",
        6: "Random movie",
        7: "Search movie",
        8: "Movies sorted by rating",
        9: "Movies sorted by year",
        10: "Filter movies",
                }

    return commands[user_input]()


def check_input():
    """
    Asks user for input, a number between 0 and 10
    Else, will continue asking for a valid input
    Returns an integer
    """
    while True:
        try:
            print_menu()
            user_input = int(input("Enter choice (0-10): "))
            assert 0 <= user_input <= 10
            return user_input
        except (ValueError, AssertionError):
            print("Invalid choice")
            continue


def print_menu():
    menu = ("\nMenu:\n"
            "0. Exit\n"
            "1. List movies\n"
            "2. Add movie\n"
            "3. Delete movie\n"
            "4. Update movie\n"
            "5. Stats\n"
            "6. Random movie\n"
            "7. Search movie\n"
            "8. Movies sorted by rating\n"
            "9. Movies sorted by year\n"
            "10. Filter movies\n")
    print(menu)


def exit():
    print("Bye!")
    sys.exit()


def main():
    """
    A command line interface with a command_dispatcher
    that performs SCRUM operations with a json file
    1. Displays a title
    2. Displays a menu with the operations available
    3. Requests and checks input from user
    4. Executes a command
    5. Menu is displayed again, asks for input again
    """
    title = "********** My Movies Database **********"
    print(title)

    while True:
        user_input = check_input()
        command_dispatcher(user_input)
        input("\nPress enter to continue ")


if __name__ == "__main__":
    main()
