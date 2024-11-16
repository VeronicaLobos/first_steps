def is_divisible_by(number, by):
''' returns True if "number" is divisible by "by" without remainder '''
    check_list = []
    if number == 2:
    ''' if the number is 2, it is the only even prime '''
        return True
        ''' then number is the prime number 2 '''
    elif number % 2 != 0:
    ''' else, if the number is not even... '''
        for i in by:
        ''' check the remainder from dividing "number" by every number in "by"... '''
            check_list.append(number % i)
            ''' and put all the remainders for that number in a list'''
        if check_list.count(0) == 0:
        ''' if we don't get a remainder equal to cero from any of the divisions... '''
            return True
            ''' then number is a prime number '''


def is_prime(number):
    ''' returns True if "number" is a prime number '''
    by = []
    for i in range(3, (int(round(number ** 0.5) + 1)), 2):
        if i % 2 != 0:
            by.append(i)
    ''' obtain a list "by" containing a range of numbers from 3 to
    the square root of "number" +1, omitting even numbers
    return is_divisible_by(number, by) '''
    # print(by) ''' for testing only '''


def primes_in_range(start, end):
    ''' prints all the prime numbers that are between "start" and "end"
    not including the number end itself
    asume "start" and "end" are int and >1, and "end" > "start" '''
    for i in range(start, end):
        ''' for each number in input range '''
        if is_prime(i):
        ''' if prime returns True '''
            print(f'The number {i} is prime')


def main():
    ''' ask the user to enter the start of the range and the end of
    the range, and print all the prime numbers within that range '''
    start_range = int(input('Enter start range: '))
    end_range = int(input('Enter end range: '))
    primes_in_range(start_range, end_range)


if __name__ == "__main__":
    main()