import requests as req

URL = "https://learningserver.masterschool.com/http-basics/get-me"

def main():
    """
    Learning the basics of a get request.
    Takes a url and adds a query string with two parameters
    via user input.
    When done correctly it will print html with a flag.
    """
    res = req.get(URL)
    # print the status response or...
    print(res)
    # ...print the status code number
    print(f"We've got code {res.status_code}, now we need parameters for the query: ")

    payload = {'name': input("What is your name? "),
            'color': input("What is your favourite color? ")}

    make_query = req.get(URL, payload)

    # show the original url with the query string attached
    print(make_query.url)
    # one option is to get the html text in a single line
    print(make_query.content)
    # another option is to get the html with line breaks
    print(make_query.text)

    print("\t\t\t*** Success! ***")

if __name__ == "__main__":
    main()
