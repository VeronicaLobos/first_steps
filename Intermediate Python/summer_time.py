def input_number():
    ''' asks for a number from the user and returns it'''
    return int(input('Enter your number: '))

def sum_user_numbers():
    ''' checks if the sum of the numbers in a loop until it
    has reached 1000 or higher and returns the final sum'''
    sum = 0
    while True:
        if sum < 1000:
            sum += input_number()
        elif sum >= 1000:
            return sum

def main():
    ''' prints a message when the sum of numbers input by the
    user reaches 1000 or higher, indicating the final sum'''
    print("Final sum: " + str(sum_user_numbers()))

if __name__ == "__main__":
    main()