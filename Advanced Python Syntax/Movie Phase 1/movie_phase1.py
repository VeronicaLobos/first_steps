def command_dictionary():
    """
    Returns a dictionary pairing the menu options
    with the functions available to the user in
    the CLI
    """
    pass


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
            break
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


def main():
    """
    A command line interface with a command_dispatcher
    that performs SCRUM operations with a json file
    """
    title = "********** My Movies Database **********"
    print(title)

    while True:
        user_input = check_input()
        # command_dispatcher(user_input)





if __name__ == "__main__":
    main()

"""
### 1

10 movies in total
In the Name of the Father (1993): 8.1
Titanic (1997): 7.9
The Shawshank Redemption (1994): 9.3
The Godfather (1972): 9.2
The Dark Knight (2008): 9.0
Schindler's List (1993): 8.9
Forrest Gump (1994): 8.8
Pulp Fiction (1994): 8.9
The Matrix (1999): 1.0
Fight Club (1999): 8.8

Press enter to continue


Title
Rating
Year of release


"""