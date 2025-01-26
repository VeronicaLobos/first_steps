import requests as req

URL = "https://fruityvice.com/api/fruit/"

URL2 = "https://fruitmap.org/"

def main():
    fruit_name = input('What fruit would you like to learn about? ')
    fruit = req.get(URL + fruit_name)
    if fruit.status_code == 200:
        print(fruit.json())
    else:
        print(f"Error: {fruit.status_code}, fruit not found")

if __name__ == "__main__":
    main()