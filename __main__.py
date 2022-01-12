import bs4
import requests

session = requests.session()


def get(url):
    return session.get(url)


def main():
    example = bs4.BeautifulSoup(get("https://example.com/").text, "html.parser")
    print(example.title.text)


if __name__ == "__main__":
    main()
