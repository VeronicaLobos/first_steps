import string
from romeo_and_juliet import PLAY

def top_50_words(dictionary_freq):
    ''' sorts a dictionary by value from highest and returns
    the first 50 items'''
    words_sorted_highest_value = sorted(dictionary_freq.items(), key = lambda item: item[1], reverse = True)
    # make a list of tuples from the dictionary sorted by value in descending order
    top_50 = dict(words_sorted_highest_value[:50])

    # make a dictionary with the first 50 items from the list
    return top_50

def dictionary_occurrences(list_of_words):
    ''' counts the number of occurrences for every word in the
    list and returns a dictionary (word, count) '''
    dict_words_count = {}
    for word in list_of_words:
    # for every word in the list ...
        if word in dict_words_count:
        # ... when the word is already in the dictionary ...
            dict_words_count[word] += 1
            # ... add 1 to the value
        elif word not in dict_words_count:
        # otherwise ...
            dict_words_count[word] = 1
            # ... add a new key with that word
    return dict_words_count


def text_to_list_of_words(text):
    ''' converts a string to a list of words, removing spaces '''
    return text.split()


def remove_uppercase(text):
    ''' converts all the characters in a string to lowercase '''
    return text.lower()


def replace_roman_num(text):
    ''' uses a dictionary to replace roman numerals for digits,
    bonus function to practice mapping :) '''
    translator = {'ACT V': 'ACT 5', 'ACT III': 'ACT 3', 'ACT II': 'ACT 2', 'ACT IV': 'ACT 4', 'ACT I': 'ACT 1', 'Scene IV': 'Scene 4', 'Scene III': 'Scene 3', 'Scene II': 'Scene 2', 'Scene I': 'Scene 1', 'Scene VI': 'Scene 6', 'Scene V': 'Scene 5'}
    # a hardcoded dictionary 'roman number' to 'digit', in the order they should be converted to avoid translation errors
    for roman, digit in translator.items():
        # for every item in the dictionary...
        text = text.replace(roman, digit)
        # ... find and replace the string from the key for the string its corresponding value, in the text
    return text


def remove_punctuation(text):
    ''' removes punctuation characters from a string '''
    translator = str.maketrans('', '', string.punctuation)
    # make an object that translates every punctuation character to an empty character ""...
    return text.translate(translator)
    # ... and return the text after applying the translate method to the text with it


def main():
    ''' a program that gets a text (string) stored in a variable
    and prints the top 50 most frequent words
    from the most frequent to the least frequent,
    along with the number of times that the word appears in the text '''

    # the first three steps will clean and prepare the string
    step_1 = remove_punctuation(PLAY)
    step_2 = replace_roman_num(step_1)
    step_3 = remove_uppercase(step_2)

    # the next steps will obtain the words from the text
    step_4 = text_to_list_of_words(step_3)

    # count the number of occurrences for each word in the text
    step_5 = dictionary_occurrences(step_4)
    result = top_50_words(step_5)

    # and finally print the result
    ''' iterates through a dictionary to print strings containing
    key and values '''
    print(f'Top 50 words in Romeo and Juliet:')
    order = 0
    for word, freq in result.items():
        order += 1
        print(f'The #{order} word is "{word}" and appears {freq} times.')

#if __name__ == "__main__":
#    main()