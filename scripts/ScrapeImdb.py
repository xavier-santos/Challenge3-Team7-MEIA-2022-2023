import csv
import json
from PyMovieDb import IMDB

imdb = IMDB()
with open("../data/all_movie_names.txt", "r") as movie_names_txt:
    with open('movies_database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date Published", "Description",
                         "Rating", "Rating Count", "Content Rating",
                         "Genre(s)", "Keywords"])
        for movie_name in movie_names_txt:
            movie = json.loads(imdb.get_by_name(movie_name.strip()))
            try:
                writer.writerow([movie["name"], movie["datePublished"], movie["description"],
                                 movie["rating"]["ratingValue"], movie["rating"]["ratingCount"], movie["contentRating"],
                                 ','.join(movie["genre"]), movie["keywords"]])
                print("Successfully Added Movie:" + movie["name"] + " from:" + movie["datePublished"])
            except:
                print("Movie Failed:" + movie_name)
