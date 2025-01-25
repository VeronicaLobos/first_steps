import requests as req

URL = "https://learningserver.masterschool.com/http-basics/post-me"

def main():
    """
    Learning the basics of a post request.
    Just like in task1
    """
    params = {"username": input("Username: "),  # 'Johana'
              "password": input("Password: ")}  # 'PostingIsCool'

    make_query = req.post(URL, params)
    print(make_query.url)
    print(make_query.text)
    print("\n\tSuccess!")

if __name__ == "__main__":
    main()
