import requests

REQUEST_URL =  "https://en.wikipedia.org/wiki/"
HTML_FILE_NAME = "wikipedia_html_template.html"
CHRS_TO_DISPLAY = 500


def preview_html_file(html_file_name, chrs_to_display):
    with open(html_file_name, 'r') as handle:
        content = handle.read()

    print(content[:chrs_to_display])


def create_html_file(html_file_name, url_text):
    with open(html_file_name, 'w', encoding="utf-8") as handle:
        handle.write(url_text)


def main():
    """
    Shows a preview of the html file from en.wikipedia chosen by the user,
    after storing the article's html in a file
    """

    search_term = str(input("What Wikipedia Article are you looking for? "))
    wikipedia_article = REQUEST_URL + search_term
    print(wikipedia_article)

    res = requests.get(wikipedia_article)
    print(res)  # or    print(res.status_code)

    get_url_text = res.text   # store the html from the web

    create_html_file(HTML_FILE_NAME, get_url_text)

    preview_html_file(HTML_FILE_NAME, CHRS_TO_DISPLAY)


if __name__ == "__main__":
    main()