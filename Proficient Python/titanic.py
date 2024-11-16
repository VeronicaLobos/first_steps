import sys
from itertools import islice
from load_data import load_data
all_data = load_data()


def ships_per_type(): # Bonus Step 2
  """
  Returns a dictionary ship-type : num_per_type
  """
  ship_type = []
  for data in all_data['data']:
    ship_type.append(data["TYPE_SUMMARY"])

  ships_per_type = {}
  for type_ in ship_type:
    if type_ not in ships_per_type:
      ships_per_type[type_] = 1
    if type_ in ships_per_type:
      ships_per_type[type_] += 1

  # print result
  print('-- Num of ships per type --')
  for key, value in ships_per_type.items():
    print(f'{key}: {value} ships')


def top_countries(num_countries):
  """
  Prints a list of top countries with the most ships,
  along with the number of ships
  """
  # make dictionary country : num of ships
  nationalities = get_nationalities()
  ships_per_country = {}

  for country in nationalities:
    if country not in ships_per_country:
      ships_per_country[country] = 1
    if country in ships_per_country:
      ships_per_country[country] += 1

  # sort dict by higher value to lowest
  sorted_ships_per_country = dict(sorted(ships_per_country.items(),
                                   key = lambda item: item[1], reverse = True))

  # slice sorted dict
  end_index = int(num_countries)
  top_countries_by_user = dict(islice(sorted_ships_per_country.items(), 0, end_index))

  # print result
  print(f'-- Top {num_countries} ships per country --')
  for key, value in top_countries_by_user.items():
    print(f'{key}: {value} ships')


def show_countries():
  """
  Prints a list of all the countries of the ships,
  without duplicates, in alphabetical order
  """
  nationalities = get_nationalities()

  for country in sorted(set(nationalities)):
    print(country)


def get_nationalities():
  """
  Returns a list with all "COUNTRY" values in all_data
  """
  nationalities = []
  for data in all_data['data']:
    nationalities.append(data["COUNTRY"])
  return nationalities


def command_dispatcher(command): # Bonus Step 1
  """
  A dictionary of commands. When the parameter contains
  a function name and a number, splits it into two arguments
  before function call
  """
  command_dict = {
    'help': help_command,
    'show_countries': show_countries,
    'top_countries': top_countries,
    'ships_per_type': ships_per_type,
    'exit': sys.exit,
  }

  arguments = command.split()
  command_name = arguments[0]

  if command_name in command_dict:
    if len(arguments) > 1:
      command_dict[command_name](arguments[1])
    else:
      command_dict[command_name]()


def help_command():
  """
  Prints a list of the available commands
  """
  print('\nAvailable commands:')
  print(' help')
  print(' show_countries')
  print(' top_countries <num_countries>')
  print(' ships_per_type')
  print(' exit')


def main():
  """
  A command line interface with a command_dispatcher
  to show info stored in a json file to the user
  """
  print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
  while True:
    user_input = input().lower()
    if user_input == 'help':
      help_command()
      command = input()
      command_dispatcher(command)
      print("\nEnter 'help' to view available commands.")
    else:
      print("Enter 'help' to view available commands.")


if __name__ == '__main__':
  main()
