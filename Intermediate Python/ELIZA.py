from itertools import chain

"""
Programming an ELIZA clone.
0. Welcomes the user and requests input
1. Asks for input
1.1 Checks if user wants to exit the program
2. Checks for certain words in user input
2.1 Creates custom prompt based on user input
3. Updates the prompt
"""

# Prints a welcome message, plus instructions
print("HELLO, I AM ELIZA. I'LL BE YOUR THERAPIST TODAY.")
print("(ENTER 'q' ANYTIME TO QUIT)")

# Sets prompt with a default message
prompt = "Is anything troubling you?"

# Sets lists of words we will search for in the input
noun_keywords = set(["mother", "Python", "the sandman"])
verb_keywords = set(["avoid", "worry", "fear", "think"])
pronouns = {
    " I ": " you ",
    " you ": " I ",
    " you": " me",  # usually at the end of a sentence
    " my ": " your ",
    " your ": " my ",
    " me": " you",
    " are ": " am ",
}

# Keeps asking user for input...
while True:
    problem = input(prompt.upper() + "\n>> ")

    # ...until user enters "q"
    if problem == "q":
        print("See you in the next session!")
        break

    # If the input is empty it will encourage the user to write
    if problem == "":
        prompt = "Our conversation is confidential, you can talk to me."
        continue

    # Sets prompt with another default message in case the user
    # input doesn't match any of the following criteria
    prompt = "Tell me more."

    # Checks for verb keywords to create a custom reply
    # this will overwrite the default prompt
    for keyword in verb_keywords:
        if keyword in problem:
            # ... slices from the first character in said keyword
            start = problem.find(keyword)
            # ... until the first dot it finds
            end = problem.find(".")
            # ... unless there is no dot
            if end == -1:
                end = len(problem)
            custom_reply = problem[start:end]

            replaced_pronouns = []
            # ... if there are pronouns in the verb custom reply *BONUS*
            for pronoun, new_pronoun in pronouns.items():
                if pronoun in custom_reply:
                    if pronoun not in replaced_pronouns:
                        # ... replaces them
                        custom_reply = custom_reply.replace(pronoun, new_pronoun)
                        # while keeping track of the ones already replaced
                        replaced_pronouns.append(new_pronoun)
                        # note: the spacing in the pronouns is relevant, to avoid
                        # words like 'care' and 'your' from turning into 'cam'
                        # or 'Ir', see pronouns dict

            # finally updates the next prompt with a custom reply based
            # on the user input
            prompt = f"Why do you {custom_reply}?"

    # Checks for noun keywords to create a custom reply, this will
    # overwrite any previous default or custom prompt
    for keyword in noun_keywords:
        if keyword in problem:
            prompt = f"What made you think of {keyword}?"
