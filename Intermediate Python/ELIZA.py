
def check_words(target, words):
    """
    Receives a list of words, checks for a match with the
    words from another list.
    Prints a message indicating if it found a match or not.
    """
    for word in words:
        if word in target:
            print("Word found!")
            break

    print("Word not found!")

def main():
    # Prints a welcome message"
    print("Hello, I am Eliza. I'll be your therapist today.")

    # Sets prompt with a default message
    prompt = "Tell me your problem (or 'q' anytime to quit): "

    # Sets a list of words to look for in user input
    keywords = set(["avoid", "worry", "fear"])

    # Keeps prompting the user...
    while True:
        user_problem = input(prompt)

        # until user inputs "q"
        if user_problem.lower() == "q":
            print("See you next time.")
            break

        # Makes a list of words from input
        words_in_problem = user_problem.split(" ")

        # Calls a word checker
        check_words(keywords, words_in_problem)


if __name__ == "__main__":
    main()
