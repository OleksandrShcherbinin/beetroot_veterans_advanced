import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup


def get_data(url):
    response = requests.get(url)
    assert response.status_code == 200, 'Bad response'
    return response.text


def parse_data(content):
    soup = BeautifulSoup(content, 'html.parser')
    author = soup.select(".ContributorLink__name")
    description = soup.select('.Formatted')
    rating = soup.select('.RatingStatistics__rating')
    genres = soup.select(".BookPageMetadataSection__genreButton .Button__labelItem")
    details = soup.select(".FeaturedDetails")
    return {
        'title': soup.title.text,
        'author': author[0].text,
        'description': description[0].text,
        'rating': rating[0].text,
        'genres': [genre.text for genre in genres],
        'details': details[0].text
    }


def save_to_json(data, filename):
    with open("files/" + filename, "w") as file:
        json.dump(data, file, indent=4)


def main():
    content = get_data('https://www.goodreads.com/book/show/1.Harry_Potter_and_the_Half_Blood_Prince')
    data = parse_data(content)
    save_to_json(data, 'harry_potter_and_the_half_blood_prince.json')
    pprint(data)


if __name__ == '__main__':
    main()
