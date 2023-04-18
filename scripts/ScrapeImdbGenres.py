import requests
from bs4 import BeautifulSoup
import csv


def get_movie_from_url(movie_url):
    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(movie_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the full summary text if there is a "More" button
    summary_text = soup.find('span', {'data-testid': 'plot-xl'}).text
    more_button = soup.find('div', {'class': 'ipc-button__text--nowrap'}, text='See full summary')
    if more_button:
        more_url = 'https://www.imdb.com' + more_button.parent['href']
        response = requests.get(more_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        summary_text = soup.find('div', {'class': 'ipc-html-content ipc-html-content--base'}).text.strip()

    movie_name = soup.select_one('h1[data-testid="hero__pageTitle"] span').text
    genres_div = soup.find('div', {'class': 'ipc-chip-list--baseAlt', 'data-testid': 'genres'})
    genre_spans = genres_div.find_all('span', {'class': 'ipc-chip__text'})
    genres = [genre_span.text for genre_span in genre_spans]

    print(movie_name)
    if "Drama" in genres:
        print("Drama is present. Not adding.")
        return None
    print(genres)
    print(summary_text)

    return (movie_name, "", summary_text, "", "", "",
            ','.join(genres), "")


def get_movies_by_genre(genre, page):
    url = "http://www.imdb.com/search/title/"
    params = {"genres": genre, "start": page, "title_type": "feature"}
    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    movies = soup.find_all("div", class_="lister-item-content")
    return movies


def main():
    with open('movies_database.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        movies = []
        for i in range(1, 25):
            movies.extend(get_movies_by_genre("fantasy", i * 50))
        for movie in movies:
            movie_url = "http://www.imdb.com" + movie.h3.a["href"]
            try:
                result = get_movie_from_url(movie_url)
                if result is not None:
                    writer.writerow(result)
            except:
                print("Error on movie: " + movie)


if __name__ == '__main__':
    main()
