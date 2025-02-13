
def main():
    # Prints a welcome message"
    print("Hello, I am Eliza. I'll be your therapist today.")

    # Sets prompt with a default message
    prompt = "Tell me your problem (or 'q' anytime to quit): "

    # Sets a list of words to look for in user input
    check: list[str] = ["avoid", "worry", "fear"]

    # Keeps prompting the user...
    while True:
        problem = input(prompt)

        # until user inputs "q"
        if problem.lower() == "q":
            print("Ok, bye!")
            break


if __name__ == "__main__":
    main()
