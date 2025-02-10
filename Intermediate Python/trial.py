
def count_vowels(string: str):

    vowel_count = 0

    vowels = set(["a", "e", "i", "o", "u"])

    for character in string.lower():
        if character in vowels:
            vowel_count += 1

    return vowel_count


def main():
    sentence = "I am a Software Engineer"
    print(count_vowels(sentence))


if __name__ == "__main__":
    main()
