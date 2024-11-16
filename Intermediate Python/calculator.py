def calculate(number_of_calcs):
  for i in range(int(number_of_calcs)):
    user_input = input("What do you want to calculate? ")
    if "+" in user_input: # sum
      num = user_input.split("+")
      print(f'The answer is {int(num[0]) + int(num[1])}')
    elif "*" in user_input: # multiplication
      num = user_input.split("*")
      print(f'The answer is {int(num[0]) * int(num[1])}')
    elif "/" in user_input: # division
      num = user_input.split("/")
      print(f'The answer is {round(int(num[0]) / int(num[1]), 2)}')
    elif "-" in user_input: # substraction
      num = user_input.split("-")
      print(f'The answer is {int(num[0]) - int(num[1])}')
    elif "~" in user_input: # integer division and remainder
      num = user_input.split("~")
      print(f'The answer is {round(float(num[0]) // float(num[1]))}')
      print(f'The remainder is {round(float(num[0]) % float(num[1]))}')

def main():
  print("Welcome to the Python calculator!")
  calculate(input("How many calculations do you want to do? "))

if __name__ == "__main__":
  main()
