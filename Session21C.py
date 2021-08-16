import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.espncricinfo.com/series/ipl-2021-1249214/points-table-standings"
    response = requests.get(url)
    print(response.text)

    # Web Scrapping :)
    # HTML Parsing

    soup = BeautifulSoup(response.text, "html.parser")

    tags = soup.find_all("h5", class_="header-title label")

    team_names = []

    for tag in tags:
        print(tag.text)
        team_names.append(tag.text.strip())

    team_names.pop(0)
    print(team_names)
    print(len(team_names))


if __name__ == '__main__':
    main()