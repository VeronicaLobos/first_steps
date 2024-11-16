def is_prime(addend):
    """
    checks if a number is prime, returns bool
    """
    if addend <= 2:
        return False
    divisor = 2
    while divisor ** 2 <= addend:
        if addend % divisor == 0:
            return False
        divisor += 1
    return True


def sum_of_two_primes(number):
    """
    finds pairs of primes which addition equals a given number,
    returns a list with every possible pair
    """
    max_range = int(number // 2) # to avoid results from repeating
    final_list = []

    for addend_1 in range(2, max_range):
        if is_prime(addend_1):
            addend_2 = number - addend_1 # finds a complementary number
            if is_prime(addend_2):
                final_list.append((addend_1, addend_2)) # *bonus step*
    return final_list


def is_input_even_int(prompt):
    """
    receives a string through an input, returns it as integer if
    input can be converted to int, otherwise keeps program from crashing
    """
    while True:
        try:
            num = int(input(prompt))
            if num > 2 and num % 2 == 0:
                return num
        except ValueError as e:
            print('Input is not an integer', e)


def print_list_of_tuples(number_from_user, result):
    """
    prints items from a list of tuples in a string
    """
    for item in result:
        print(f'The number {number_from_user} equals to the sum of {item[0]} and {item[1]}')


def main():
    """
    a program that checks if an even number greater than 2
    is the result of adding two prime numbers
    """
    number_from_user = is_input_even_int("Enter a number: ")
    result = sum_of_two_primes(number_from_user)
    print_list_of_tuples(number_from_user, result)

if __name__ == "__main__":
    main()
